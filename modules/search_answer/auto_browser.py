from playwright.async_api import async_playwright
from pathlib import Path

class AutoBrowser:
    @staticmethod
    async def wakeup(search: str, output_file: str = "itog.txt"):
        answers_dir = Path(__file__).parent.parent.parent.parent / "damn_answers1"
        answers_dir.mkdir(exist_ok=True)
        output_path = answers_dir / output_file
        
        async with async_playwright() as l:
            browser = await l.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://duckduckgo.com/")
            query = page.locator("input[name='q']")
            await query.fill(search)
            await query.press("Enter")
            await page.wait_for_selector("article", timeout=5000)
            results = await page.query_selector_all("article")
            
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(f"Результаты поиска по запросу: '{search}'\n")
                file.write(f"Всего найдено результатов: {len(results)}\n")
                file.write("=" * 60 + "\n\n")
                
                for i, answer in enumerate(results, 1):
                    link_el = await answer.query_selector("a[data-testid='result-title-a']")
                    
                    if link_el:
                        title = await link_el.text_content()
                        url = await link_el.get_attribute("href")
                        file.write(f"РЕЗУЛЬТАТ #{i}\n")
                        file.write(f"┌{'─' * 50}\n")
                        file.write(f"│ Заголовок: {title}\n")
                        file.write(f"│ URL: {url}\n")
                        file.write(f"└{'─' * 50}\n\n")

            await browser.close()
            
            
