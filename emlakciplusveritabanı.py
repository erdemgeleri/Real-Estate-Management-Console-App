import psycopg2

class Emlak:
    def __init__(self, conn):
        self.conn = conn

    def enter_home_infs(self):
        print("\n--- Yeni Ev Kaydı ---")
        title = input('Başlık: ')
        price = input('Fiyat: ')
        number_of_rooms = input('Oda Sayısı: ')
        situation = input('Durum (Satılık/Kiralık): ')
        desc = input('Açıklama: ')

        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO emlak (title, price, number_of_rooms, situation, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (title, price, number_of_rooms, situation, desc))
            self.conn.commit()
        print('✅ Yeni ev başarıyla kaydedildi!\n')

    def get_all_homes(self):
        print("\n--- Kayıtlı Evler ---")
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM emlak")
            homes = cursor.fetchall()
            if not homes:
                print("❌ Kayıtlı ev bulunmamaktadır.\n")
            else:
                for home in homes:
                    print(f"""
------------------------------
🏠 ID: {home[0]}
📌 Başlık: {home[1]}
💰 Fiyat: {home[2]} TL
🛋️ Oda Sayısı: {home[3]}
📄 Durum: {home[4]}
📝 Açıklama: {home[5]}
------------------------------
                    """)
        print()

    def delete_home(self, home_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM emlak WHERE id = %s", (home_id,))
            self.conn.commit()
            print(f"✅ ID {home_id} olan ev başarıyla silindi!\n")

    def update_home(self, home_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM emlak WHERE id = %s", (home_id,))
            home = cursor.fetchone()
            if not home:
                print("❌ Geçersiz ID.\n")
                return

            print("\n--- Ev Güncelleme ---")
            title = input(f"Başlık ({home[1]}): ") or home[1]
            price = input(f"Fiyat ({home[2]}): ") or home[2]
            number_of_rooms = input(f"Oda Sayısı ({home[3]}): ") or home[3]
            situation = input(f"Durum ({home[4]}): ") or home[4]
            desc = input(f"Açıklama ({home[5]}): ") or home[5]

            cursor.execute("""
                UPDATE emlak
                SET title = %s, price = %s, number_of_rooms = %s, situation = %s, description = %s
                WHERE id = %s
            """, (title, price, number_of_rooms, situation, desc, home_id))
            self.conn.commit()
            print(f"✅ ID {home_id} olan ev başarıyla güncellendi!\n")


conn = psycopg2.connect(
    dbname="emlakci",
    user="postgres",
    password="bil123",
    host="localhost",
    port="5432"
)

emlak_app = Emlak(conn)

while True:
    print("""
===========================
🏠 EMLAKÇI UYGULAMASI
===========================
1️⃣ Kayıtlı evleri görüntüle
2️⃣ Yeni ev kaydı ekle
3️⃣ Kayıtlılardan ev sil
4️⃣ Kayıtlılardan ev güncelle
5️⃣ Çıkış yap
===========================
    """)
    secim = input('Seçiminiz: ')

    if secim == '1':
        emlak_app.get_all_homes()
    elif secim == '2':
        emlak_app.enter_home_infs()
    elif secim == '3':
        home_id = int(input("Silmek istediğiniz evin ID'sini girin: "))
        emlak_app.delete_home(home_id)
    elif secim == '4':
        home_id = int(input("Güncellemek istediğiniz evin ID'sini girin: "))
        emlak_app.update_home(home_id)
    elif secim == '5':
        print("👋 Çıkış yapılıyor... Hoşça kalın!")
        break
    else:
        print("❌ Geçersiz seçim, tekrar deneyin.\n")
