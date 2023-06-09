import datetime
import pandas as pd

try:
    csv_path = "contacts.csv"

    today = datetime.date.today().strftime("%Y%m%d")
    vcf_path = f"{today}_vcard.vcf"

    df = pd.read_csv(csv_path, encoding="utf-8")

    def generate_vcard(row):
        vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{row['family']};{row['first']};;;\n"
        vcard += f"X-PHONETIC-FIRST-NAME:{row['first_kana']}\n"
        vcard += f"X-PHONETIC-LAST-NAME:{row['family_kana']}\n"
        vcard += f"EMAIL;TYPE=INTERNET:{row['email']}\n"
        vcard += f"TEL;TYPE=CELL:{row['tel_with_bar']}\n"
        vcard += "END:VCARD\n"
        return vcard

    # VCファイルを書き込む
    with open(vcf_path, "w", encoding="shift_jis") as vcf_file:
        for index, row in df.iterrows():
            vcard_string = generate_vcard(row)
            vcf_file.write(vcard_string)
            vcf_file.write("\n")
except Exception as e:
    print(e)
    input()
