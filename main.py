import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Lütfen .env dosyası içerisine GEMINI_API_KEY tanımlayın!")

# Gemini Modelini Tanımlıyoruz
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=api_key)

print(
    "🛡️ Saf LangChain ve Gemini ile Kontrollü SDLC Aşamaları Başlatılıyor...\n"
)


def ask_human_approval(step_name: str, content: str) -> bool:
    print(f"\n{'='*20} ONAY KAPISI: {step_name} {'='*20}")
    print(f"\n{content[:1000]}...\n[Çıktının devamı gizlendi]")
    print(f"{'='*50}")
    while True:
        choice = (
            input(
                f"'{step_name}' aşamasını onaylıyor musunuz? (e: Evet / h: Hayır"
                " - Tekrar Üret): "
            )
            .strip()
            .lower()
        )
        if choice == "e":
            print(f"✅ '{step_name}' onaylandı. Sonraki aşamaya geçiliyor...\n")
            return True
        elif choice == "h":
            print(f"❌ '{step_name}' reddedildi. Yeniden üretiliyor...\n")
            return False
        else:
            print("Lütfen 'e' veya 'h' girin.")


def clean_response(response_content) -> str:
    """Model çıktısının her koşulda string olmasını garanti eder."""
    if isinstance(response_content, list):
        return "".join(
            item.get("text", str(item)) if isinstance(item, dict) else str(item)
            for item in response_content
        )
    return str(response_content)


def run_pure_sdlc(project_idea: str):
    # Aşama 1: PRD
    print("\n📝 [Aşama 1/4] Ürün Yöneticisi PRD hazırlıyor...")
    prompt_prd = f"Sen kıdemli bir Ürün Yöneticisisin. Şu fikir için detaylı bir Ürün Gereksinim Belgesi (PRD) oluştur: {project_idea}"

    prd_result = None
    while not prd_result:
        raw_res = llm.invoke(prompt_prd).content
        res = clean_response(raw_res)
        if ask_human_approval("Ürün Gereksinim Belgesi (PRD)", res):
            prd_result = res
            with open("1_prd.md", "w", encoding="utf-8") as f:
                f.write(prd_result)

    # Aşama 2: Mimari
    print("\n🏗️ [Aşama 2/4] Yazılım Mimarı sistemi tasarlıyor...")
    prompt_arch = f"Sen kıdemli bir Yazılım Mimarısın. Şu PRD'ye dayanarak sistem mimarisini ve dosya yapısını çıkar:\n\n{prd_result}"

    arch_result = None
    while not arch_result:
        raw_res = llm.invoke(prompt_arch).content
        res = clean_response(raw_res)
        if ask_human_approval("Mimari Tasarım", res):
            arch_result = res
            with open("2_architecture.md", "w", encoding="utf-8") as f:
                f.write(arch_result)

    # Aşama 3: Kodlama
    print("\n💻 [Aşama 3/4] Kıdemli Geliştirici kodu yazıyor...")
    prompt_code = f"Sen kıdemli bir Yazılımcısın. Şu mimari ve PRD'ye dayanarak projenin ana Python kodunu Markdown kod bloğu içinde yaz:\n\nPRD:\n{prd_result}\n\nMimari:\n{arch_result}"

    code_result = None
    while not code_result:
        raw_res = llm.invoke(prompt_code).content
        res = clean_response(raw_res)
        if ask_human_approval("Yazılım Kodu", res):
            code_result = res
            with open("3_code.md", "w", encoding="utf-8") as f:
                f.write(code_result)

    # Aşama 4: QA / Test
    print("\n🧪 [Aşama 4/4] QA Uzmanı test senaryoları hazırlıyor...")
    prompt_test = f"Sen bir Kalite Güvence (QA) Uzmanısın. Geliştiricinin yazdığı şu kodu incele ve unittest ile birim testlerini yaz:\n\nKod:\n{code_result}"

    test_result = None
    while not test_result:
        raw_res = llm.invoke(prompt_test).content
        res = clean_response(raw_res)
        if ask_human_approval("Test ve Kalite Raporu", res):
            test_result = res
            with open("4_qa_report.md", "w", encoding="utf-8") as f:
                f.write(test_result)

    print(
        "\n🎉 Tebrikler! Tüm SDLC süreci başarıyla tamamlandı ve dosyalara"
        " kaydedildi."
    )


if __name__ == "__main__":
    user_idea = (
        "Kullanıcıların notlarını ekleyip listeleyebileceği basit bir"
        " command-line (CLI) not alma uygulaması."
    )
    run_pure_sdlc(user_idea)