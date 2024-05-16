import pefile
import sys

def extract_iat(pe_file):
    try:
        # Muat file PE
        pe = pefile.PE(pe_file)

        # Periksa apakah file tersebut memiliki tabel impor
        if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            print(f"IAT untuk {pe_file}:")

            # Iterasi atas setiap entri dalam tabel impor
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print(f"Imports dari {entry.dll.decode()}:")
                for imp in entry.imports:
                    address = hex(imp.address)
                    name = imp.name.decode() if imp.name else 'Ordinal Import'
                    print(f"    {address} {name}")
        else:
            print("Tidak ada impor yang ditemukan.")
    
    except Exception as e:
        print(f"Kesalahan saat memproses file: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        extract_iat(sys.argv[1])
    else:
        print("Harap berikan path ke file PE sebagai argumen.")
