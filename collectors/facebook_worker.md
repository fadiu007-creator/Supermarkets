# Facebook collection worker

The production worker must receive page/post content through a permitted public interface. It should then:

1. identify the configured supermarket page;
2. retain page/post/source URLs;
3. retain publication time when available;
4. parse EUR prices from post text;
5. preserve original text for auditability;
6. pass candidates to the normalizer;
7. persist observations with collection timestamps.

## Access boundary

This worker must not automate a personal Facebook login, reuse session cookies, bypass CAPTCHA, circumvent access controls, or evade platform rate limits. If the public interface does not provide the content, mark the source unavailable and continue with another permitted source.

## Browser connector option

A separately authorized browser session can be used to inspect a page manually or through a permitted automation integration. The application should receive only the public content needed for processing rather than storing browser credentials.
