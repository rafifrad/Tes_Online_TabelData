import requests

def cek_berita():
    api_key = 'abf60ddff4804a2fb712425aa29b5ed0'
    base_url = 'https://newsapi.org/v2/top-headlines'

    print("pilih kategori berita: ")
    print("[1] Teknologi")
    print("[2] Bisnis")
    print("[3] Olahraga")
    print("[4] Kesehatan")
    print("[5] Sains")

    pilihan = input("Masukkan pilihan Anda (1-5): ")

    kategori = {
        '1': 'technology',
        '2': 'business',
        '3': 'sports',
        '4': 'health',
        '5': 'science'
    }

    if pilihan in kategori:
        
        params = {
            'country': 'us',
            'category': kategori[pilihan],
            'pageSize': 5,  
            'apiKey': api_key
        }

        try:
            response = requests.get(base_url, params=params)
            data_berita = response.json()

            print(f"\nBerikut adalah top 5 berita di kategori {kategori[pilihan]}:\n")

            artikel_list = data_berita['articles']

            nomor = 1
            for artikel in artikel_list:
                judul = artikel['title']
                print(f"{nomor} - {judul}")
                nomor += 1
                
        except Exception as e:
            print("terjadi kesalahan. coba lagi")
            
    else:
        print("\nPilihan tidak valid. harap masukkan ulang angka 1-5.")

cek_berita()