from playwright.sync_api import sync_playwright

class AutoBrowser:
    def wakeup(self):
        results = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            query = input()
            i = 0

            page.goto(f"https://duckduckgo.com/search?q={query}")
            page.wait_for_selector("#search")

            for answer in page.query_selector_all("g")[:7]:
                try:
                    title = answer.query_selector("h3").inner_text()
                    url = answer.query_selector("a").get_attribute("href")
                    results.append({"title": title, "url": url})
                except:
                    print("Не получилось вывести сайт", i)
                    i += 1
                    continue

            browser.close
        return results
