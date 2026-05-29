content = "baseURL = 'https://isabell-furkert-129.github.io/isabells-portfolio/'\nlocale = 'de-at'\ntitle = 'Isabells Portfolio'\ntheme = 'ananke'\n"
with open('hugo.toml', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)