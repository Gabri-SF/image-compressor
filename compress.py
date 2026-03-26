import os
import io
import argparse
from PIL import Image, ImageOps

# Formatos suportados
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

# Pastas a ignorar
IGNORED_DIRS = {
    "node_modules",
    ".git",
    "dist",
    "build",
    "__pycache__",
    ".next",        
    ".nuxt",        
    ".output",      
    "out",          
    ".cache",       
    "coverage"
}


def compress_image(image_path, quality, max_width, max_height, dry_run):
    try:
        original_size = os.path.getsize(image_path)

        with Image.open(image_path) as img:
            original_format = img.format

            # Corrigir orientação
            img = ImageOps.exif_transpose(img)

            # Redimensionar opcional
            if max_width or max_height:
                img.thumbnail((max_width or img.width, max_height or img.height))

            save_kwargs = {}

            if original_format in ["JPEG", "JPG"]:
                save_kwargs["quality"] = quality
                save_kwargs["optimize"] = True
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

            elif original_format == "WEBP":
                save_kwargs["quality"] = quality
                save_kwargs["method"] = 6
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

            elif original_format == "PNG":
                save_kwargs["optimize"] = True
                save_kwargs["compress_level"] = int((100 - quality) / 10)
                # PNG mantém transparência

            if dry_run:
                buffer = io.BytesIO()
                img.save(buffer, format=original_format, **save_kwargs)
                new_size = buffer.tell()
            else:
                # Comprimir em memória
                buffer = io.BytesIO()
                img.save(buffer, format=original_format, **save_kwargs)
                compressed_size = buffer.tell()

                # Só sobrescrever se reduzir tamanho
                if compressed_size < original_size:
                    with open(image_path, "wb") as f:
                        f.write(buffer.getvalue())
                    new_size = compressed_size
                else:
                    new_size = original_size

        savings = original_size - new_size

        print(f"{'🧪 [DRY]' if dry_run else '✔'} {image_path}")
        print(f"   {original_size/1024:.1f}KB → {new_size/1024:.1f}KB (↓ {savings/1024:.1f}KB)")

    except Exception as e:
        print(f"✖ Erro em {image_path}: {e}")


def process_folder(folder, quality, max_width, max_height, dry_run):
    total = 0

    for root, dirs, files in os.walk(folder):
        # Ignorar pastas de build/cache
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith(".")]

        for file in files:
            if file.lower().endswith(SUPPORTED_FORMATS):
                full_path = os.path.join(root, file)
                print(f"\n📸 A processar: {full_path}")
                compress_image(
                    full_path,
                    quality,
                    max_width,
                    max_height,
                    dry_run
                )
                total += 1

    print(f"\n✅ Total de imagens processadas: {total}")


def main():
    parser = argparse.ArgumentParser(description="Comprimir imagens numa pasta")

    parser.add_argument("path", help="Caminho para a pasta de imagens")
    parser.add_argument("--quality", type=int, default=70, help="Qualidade (0-100)")
    parser.add_argument("--max-width", type=int, help="Largura máxima")
    parser.add_argument("--max-height", type=int, help="Altura máxima")
    parser.add_argument("--dry-run", action="store_true", help="Simular sem alterar ficheiros")

    args = parser.parse_args()

    folder_path = os.path.abspath(args.path)

    if not os.path.exists(folder_path):
        print(f"Erro: caminho não existe -> {folder_path}")
        return

    print(f"\n📂 Pasta: {folder_path}")
    print(f"⚙️ Qualidade: {args.quality}")
    if args.dry_run:
        print("🧪 Modo DRY-RUN (sem alterações)\n")

    process_folder(
        folder_path,
        args.quality,
        args.max_width,
        args.max_height,
        args.dry_run
    )


if __name__ == "__main__":
    main()