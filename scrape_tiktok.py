from playwright.sync_api import sync_playwright
import time

def scrape_tiktok_profile(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(f'https://www.tiktok.com/@{username}')
        time.sleep(5)

        for _ in range(5):
            page.keyboard.press('End')
            time.sleep(2)

        video_elements = page.locator('a[href^="/video/"]')
        timestamps = page.locator('span[data-e2e="video-time"]')

        video_urls = [el.get_attribute('href') for el in video_elements.all()]
        timestamp_texts = [el.inner_text() for el in timestamps.all()]

        if video_urls:
            for url, timestamp in zip(video_urls, timestamp_texts):
                print(f'URL: {url} | Timestamp: {timestamp}')
        else:
            print("No posts found.")

        browser.close()

if __name__ == '__main__':
    username = 'postmalone'
    scrape_tiktok_profile(username)
