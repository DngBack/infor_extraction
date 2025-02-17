from __future__ import annotations

import asyncio

from crawlee.beautifulsoup_crawler import BeautifulSoupCrawler
from crawlee.beautifulsoup_crawler import BeautifulSoupCrawlingContext


async def main() -> None:
    crawler = BeautifulSoupCrawler(
        # Limit the crawl to max requests.
        # Remove or increase it for crawling all links.
        max_requests_per_crawl=10,
    )

    # Define the default request handler,
    # which will be called for every request.
    @crawler.router.default_handler
    async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
        context.log.info(f'Processing {context.request.url} ...')

        # Enqueue all links found on the page.
        await context.enqueue_links()

    # Run the crawler with the initial list of requests.
    await crawler.run(['https://crawlee.dev'])


if __name__ == '__main__':
    asyncio.run(main())
