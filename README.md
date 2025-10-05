# Protocol Wrapper for LLMs to play Go (Weiqi/Baduk) ○●  
> [!IMPORTANT]
> **📦 This project has moved to a new independent repository: [viczommers/go-bot-llm](https://github.com/viczommers/go-bot-llm)**  
> Orinial engine was forked from [maksimKorzh/wally](https://github.com/maksimKorzh/wally)
 
[GTP (Go Text Protocol)](https://senseis.xmp.net/?GoTextProtocol) engine implementation to connect LLMs to [Sabaki GUI](https://github.com/SabakiHQ/Sabaki)
## Supports
- Azure OpenAI GPT-4o (2024-12-01-preview)

##  HOWTO
- `MAX_RETRIES_PER_GAME` var controls total number of illegal moves allowed (up to 3 attempts per game, then automatic resignation)

## Wally (Mechanical AI)
Reconstruction of the Wally - simple GO program written by Jonathan K. Millen for KIM-1<br>
Wally is a GTP engine that needs GUI to tun under,<br>
tested with fantastic cross-platform Sabaki GUI:<br>
https://github.com/SabakiHQ/Sabaki

- Original article https://archive.org/details/byte-magazine-1981-04/page/n101/mode/2up
