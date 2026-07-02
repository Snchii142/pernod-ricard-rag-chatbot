"""
UPDATED source list for Pernod Ricard RAG Knowledge Base

Key fixes vs original:
  - pernod-ricard.com: /en/about-us/ → /en/our-group/  (site restructured)
  - pernod-ricard.com: /en/sustainability/ → /en/sustainability-responsibility/
  - pernod-ricard.com: /en/our-markets/asia/india/ → /en/locations/india/
  - malibu-drinks.com domain defunct → replaced with correct working alternatives
"""


URLS = {

    # ------------------------------------------------------------------
    # 1. COMPANY INFORMATION
    # ------------------------------------------------------------------
    "company_info": [
        {
            "url": "https://www.pernod-ricard.com/en/our-group/our-history",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/our-group/our-governance",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/our-group/our-vision",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/our-group/our-role-in-society",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Pernod_Ricard",
            "brand": "Pernod Ricard",
            "source": "wikipedia",
        },
    ],

    # ------------------------------------------------------------------
    # 2. BRAND PORTFOLIO  (brand sites + Wikipedia fallbacks)
    # ------------------------------------------------------------------
    "brand_portfolio": [

        # --- Absolut ---
        {
            "url": "https://www.absolut.com/en/",
            "brand": "Absolut",
            "source": "absolut.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Absolut_Vodka",
            "brand": "Absolut",
            "source": "wikipedia",
        },

        # --- Chivas Regal ---
        {
            "url": "https://www.chivas.com/en-GB/",
            "brand": "Chivas Regal",
            "source": "chivas.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Chivas_Regal",
            "brand": "Chivas Regal",
            "source": "wikipedia",
        },

        # --- Jameson ---
        {
            "url": "https://www.jamesonwhiskey.com/en/",
            "brand": "Jameson",
            "source": "jamesonwhiskey.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Jameson_whiskey",
            "brand": "Jameson",
            "source": "wikipedia",
        },

        # --- The Glenlivet ---
        {
            "url": "https://www.theglenlivet.com/en-gb/",
            "brand": "The Glenlivet",
            "source": "theglenlivet.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/The_Glenlivet",
            "brand": "The Glenlivet",
            "source": "wikipedia",
        },

        # --- Beefeater ---
        {
            "url": "https://www.beefeatergin.com/en-gb/",
            "brand": "Beefeater",
            "source": "beefeatergin.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Beefeater_gin",
            "brand": "Beefeater",
            "source": "wikipedia",
        },

        # --- Ballantine's ---
        {
            "url": "https://www.ballantines.com/en/",
            "brand": "Ballantine's",
            "source": "ballantines.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Ballantine%27s",
            "brand": "Ballantine's",
            "source": "wikipedia",
        },

        # --- Royal Salute ---
        {
            "url": "https://www.royalsalute.com/en-gb/",
            "brand": "Royal Salute",
            "source": "royalsalute.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Royal_Salute",
            "brand": "Royal Salute",
            "source": "wikipedia",
        },

        # --- Malibu  ← domain was wrong, malibu-drinks.com is defunct ---
        # Wikipedia is the most reliable source here
        {
            "url": "https://en.wikipedia.org/wiki/Malibu_(drink)",
            "brand": "Malibu",
            "source": "wikipedia",
        },

        # --- Kahlúa ---
        {
            "url": "https://www.kahlua.com/en/",
            "brand": "Kahlúa",
            "source": "kahlua.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Kahl%C3%BAa",
            "brand": "Kahlúa",
            "source": "wikipedia",
        },

        # --- Mumm ---
        {
            "url": "https://www.mumm.com/en/",
            "brand": "Mumm",
            "source": "mumm.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/G.H._Mumm_et_Cie",
            "brand": "Mumm",
            "source": "wikipedia",
        },

        # --- Perrier-Jouët ---
        {
            "url": "https://www.perrier-jouet.com/en-gb/",
            "brand": "Perrier-Jouët",
            "source": "perrier-jouet.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Perrier-Jou%C3%ABt",
            "brand": "Perrier-Jouët",
            "source": "wikipedia",
        },

        # --- Martell ---
        {
            "url": "https://www.martell.com/en-gb/",
            "brand": "Martell",
            "source": "martell.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Martell_(cognac)",
            "brand": "Martell",
            "source": "wikipedia",
        },

        # --- Havana Club ---
        {
            "url": "https://www.havana-club.com/en-gb/",
            "brand": "Havana Club",
            "source": "havana-club.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Havana_Club",
            "brand": "Havana Club",
            "source": "wikipedia",
        },

        # --- Monkey 47 ---
        {
            "url": "https://www.monkey47.com/en/",
            "brand": "Monkey 47",
            "source": "monkey47.com",
        },

        # --- Aberlour ---
        {
            "url": "https://www.aberlour.com/en-gb/",
            "brand": "Aberlour",
            "source": "aberlour.com",
        },

        # --- Malfy Gin ---
        {
            "url": "https://www.malfy-gin.com/",
            "brand": "Malfy Gin",
            "source": "malfy-gin.com",
        },

        # --- Lillet ---
        {
            "url": "https://www.lillet.com/en",
            "brand": "Lillet",
            "source": "lillet.com",
        },

        # --- Pernod Ricard brand portfolio overview page ---
        {
            "url": "https://www.pernod-ricard.com/en/our-brands",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
    ],

    # ------------------------------------------------------------------
    # 3. SUSTAINABILITY & CSR
    # ------------------------------------------------------------------
    "sustainability": [
        {
            "url": "https://www.pernod-ricard.com/en/sustainability-responsibility/our-roadmap",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/sustainability-responsibility/responsible-hosting",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/sustainability-responsibility/nurturing-terroir",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/sustainability-responsibility/circular-making",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://www.pernod-ricard.com/en/sustainability-responsibility/valuing-people",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
    ],

    # ------------------------------------------------------------------
    # 4. TRADE, RETAIL & INDIA MARKET
    # ------------------------------------------------------------------
    "trade_retail": [
        {
            "url": "https://www.pernod-ricard.com/en/locations/india",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
        {
            "url": "https://en.wikipedia.org/wiki/Pernod_Ricard_India",
            "brand": "Pernod Ricard India",
            "source": "wikipedia",
        },
        {
            "url": "https://www.pernod-ricard.com/en/locations/travel-retail",
            "brand": "Pernod Ricard",
            "source": "pernod-ricard.com",
        },
    ],

    # ------------------------------------------------------------------
    # 5. DIFFORD'S GUIDE — tasting notes, cocktails, awards
    # ------------------------------------------------------------------
    "tasting_cocktails": [
        {
            "url": "https://www.diffordsguide.com/producers/pernod-ricard",
            "brand": "Pernod Ricard",
            "source": "diffordsguide.com",
        },
        {
            "url": "https://www.diffordsguide.com/beer-wine-spirits/category/vodka/absolut",
            "brand": "Absolut",
            "source": "diffordsguide.com",
        },
        {
            "url": "https://www.diffordsguide.com/beer-wine-spirits/category/gin/beefeater",
            "brand": "Beefeater",
            "source": "diffordsguide.com",
        },
        {
            "url": "https://www.diffordsguide.com/beer-wine-spirits/category/irish-whiskey/jameson",
            "brand": "Jameson",
            "source": "diffordsguide.com",
        },
        {
            "url": "https://www.diffordsguide.com/beer-wine-spirits/category/scotch-whisky/chivas-regal",
            "brand": "Chivas Regal",
            "source": "diffordsguide.com",
        },
        {
            "url": "https://www.diffordsguide.com/beer-wine-spirits/category/coffee-liqueur/kahlua",
            "brand": "Kahlúa",
            "source": "diffordsguide.com",
        },
        {
            "url": "https://www.diffordsguide.com/beer-wine-spirits/category/cognac/martell",
            "brand": "Martell",
            "source": "diffordsguide.com",
        },
    ],

    # ------------------------------------------------------------------
    # 6. GUARDRAILS — responsible drinking redirect resources
    # ------------------------------------------------------------------
    "guardrails": [
        {
            "url": "https://www.drinkaware.co.uk/",
            "brand": "Drinkaware",
            "source": "drinkaware.co.uk",
        },
        {
            "url": "https://www.niaaa.nih.gov/",
            "brand": "NIAAA",
            "source": "niaaa.nih.gov",
        },
        {
            "url": "https://www.iard.org/",
            "brand": "IARD",
            "source": "iard.org",
        },
    ],
}