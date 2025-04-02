5%def classify_news(headline):
    sectors = {
    "automobile": ["tesla", "ev", "car", "vehicle", "automaker", "ford", "bmw", "audi", "maruti", "tata motors", "mahindra", "bajaj", "ashok leyland", "hero", "royal enfield"],
    
    "banking": ["rbi", "bank", "interest", "loan", "finance", "credit", "monetary", "nbfc", "hdfc", "sbi", "icici", "axis bank", "paytm", "upi", "digital banking"],
    
    "technology": ["ai", "software", "google", "apple", "microsoft", "innovation", "startup", "it", "infosys", "tcs", "wipro", "hcl", "zoho", "fintech", "saas"],
    
    "healthcare": ["vaccine", "hospital", "covid", "doctor", "medicine", "pharma", "apollo", "fortis", "aiims", "ayushman", "healthtech", "biocon", "cipla", "sun pharma"],
    
    "energy": ["oil", "gas", "solar", "renewable", "power", "electricity", "reliance", "ntpc", "coal", "adani power", "thermal", "wind energy", "green hydrogen"],
    
    "telecom": ["jio", "airtel", "vodafone", "5g", "network", "bsnl", "vi", "broadband", "fiber", "spectrum auction", "telecom policy"],
    
    "agriculture": ["farmer", "crop", "fertilizer", "pesticide", "mandi", "fci", "organic", "irrigation", "agribusiness", "wheat", "rice", "sugarcane", "amul", "dairy"],
    
    "real estate": ["property", "housing", "construction", "land", "rera", "builder", "infrastructure", "lodha", "godrej properties", "dlf", "metro"],
    
    "retail": ["ecommerce", "flipkart", "amazon", "mall", "fmcg", "big bazaar", "reliance retail", "dmart", "online shopping", "kirana"],
    
    "aviation": ["air india", "indigo", "spicejet", "airport", "airline", "jet airways", "udaan", "dgca", "airfare", "flight", "boeing", "airbus"],
    
    "defence": ["drdo", "isro", "missile", "army", "navy", "air force", "rafale", "hal", "bharat dynamics", "defence production", "border security"],
    
    "tourism": ["tourism", "india tourism", "travel", "hotel", "flight", "resort", "tour operator", "holiday packages", "monuments", "heritage", "taj mahal", "goa"],
    
    "education": ["school", "college", "university", "edtech", "online learning", "students", "entrance exam", "ncert", "cbse", "ugc", "iit", "education policy"],
    
    "manufacturing": ["industry", "plant", "production", "automation", "factory", "machinery", "steel", "textiles", "chemical", "cement", "auto components"],
    
    "financial services": ["insurance", "mutual fund", "investment", "stocks", "equity", "debt", "financial advisor", "tax", "retirement", "financial planning", "share market"],
    
    "media & entertainment": ["film", "bollywood", "tv", "media", "content", "OTT", "digital media", "radio", "music", "event", "advertising", "television", "news", "streaming"],
    
    "food & beverages": ["food","milkymist" ,"restaurant", "catering", "snacks", "beverages", "organic food", "swiggy", "zomato", "packaged food", "beverage", "fmcg", "amul"],
    
    "logistics & transportation": ["transport", "logistics", "delivery", "supply chain", "shipping", "truck", "railway", "air cargo", "logistics company", "shipping industry"],
    
    "fashion & apparel": ["fashion", "clothing", "apparel", "textiles", "ethnic wear", "brands", "retail", "footwear", "designer", "saree", "t-shirt", "jeans", "store", "fabrics"],
    
    "construction": ["real estate", "building", "construction", "cement", "infrastructure", "realty", "high-rise", "residential", "commercial", "builders", "renovation"],
    
    "transportation": ["train", "bus", "rail", "metro", "vehicle", "roadways", "public transport", "cargo", "logistics", "air transport", "airport", "buses", "auto rickshaw"]
}

    
    headline = headline.lower()
    
    for sector, keywords in sectors.items():
        if any(keyword in headline for keyword in keywords):
            return sector
    
    return "unknown"


while True:
    news = input("Enter news headline (or type 'exit' to quit): ").lower()  # Convert input to lowercase
    if news == "exit":
        break
    print(f"{news} -> {classify_news(news)}")
