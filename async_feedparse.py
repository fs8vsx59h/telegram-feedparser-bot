import feedparser
import asyncio


async def async_nyaa_parse(url):
  loop = asyncio.get_event_loop()
  rss_content = await loop.run_in_executor(None, feedparser.parse, url)
  link_list = []
  for entry in rss_content.entries:
    if 'link' in entry:
      link_list.append(entry.link)
  return link_list


async def test():
  url = 'https://nyaa.si/?page=rss&q=conan&c=0_0&f=0'
  result = await async_nyaa_parse(url)
  print(result)


if __name__ == "__main__":
  asyncio.run(test())
