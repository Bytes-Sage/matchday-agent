"""All 16 host cities with unique safety, weather, tips, and emergency data."""

CITIES_DATA = [
    {
        "_id": "east-rutherford", "name": "East Rutherford / New York Metro", "state": "NJ", "country": "USA",
        "timezone": "America/New_York", "currency": "USD", "language": "English",
        "safety": ["Avoid Penn Station area late at night", "Use official yellow cabs or rideshare apps", "Keep valuables secure on the subway", "Times Square area is tourist-heavy — watch for pickpockets"],
        "weather": "Hot and humid summers, 80-90°F (27-32°C). Occasional afternoon thunderstorms. Sunscreen essential.",
        "localTips": ["Take the NJ Transit train to the stadium — driving is a nightmare", "Grab a slice of pizza from a local spot, not a chain", "The Meadowlands area has limited dining — eat in Manhattan before heading out", "Download the NJ Transit app for live train schedules", "Bring a portable charger — cell service gets spotty with 80K fans"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Hackensack University Medical Center", "embassy": "Check nyc.gov for consulate locations"},
        "fanExperience": "The energy of New York City combined with the massive MetLife Stadium creates an unmatched atmosphere. Fan zones in Times Square and Liberty State Park."
    },
    {
        "_id": "inglewood", "name": "Inglewood / Los Angeles", "state": "CA", "country": "USA",
        "timezone": "America/Los_Angeles", "currency": "USD", "language": "English/Spanish",
        "safety": ["Avoid walking alone in Inglewood after dark", "Use rideshare or Metro — don't drink and drive", "Stay hydrated — dehydration is common in the dry heat", "Sunscreen is mandatory — LA sun is intense"],
        "weather": "Warm and dry, 75-85°F (24-29°C). Almost no rain in summer. Very sunny — UV index high.",
        "localTips": ["LA traffic is legendary — leave 3+ hours early for the game", "Try authentic Mexican food on Cesar Chavez Ave in East LA", "SoFi is indoor/outdoor — it won't rain but the sun can be brutal on the open side", "Rent a scooter to explore the Hollywood area", "Beach cities (Santa Monica, Venice) are a 20-min drive from the stadium"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Centinela Hospital Medical Center", "embassy": "LA has consulates for most countries on Wilshire Blvd"},
        "fanExperience": "Hollywood glamour meets world football. Fan zones on Santa Monica Beach and in Downtown LA. Celebrity sightings likely."
    },
    {
        "_id": "arlington", "name": "Arlington / Dallas-Fort Worth", "state": "TX", "country": "USA",
        "timezone": "America/Chicago", "currency": "USD", "language": "English/Spanish",
        "safety": ["Heat exhaustion is a real risk — drink water constantly", "Arlington has limited public transit — plan your ride in advance", "Keep car windows cracked in parking lots — interior temps can reach 150°F"],
        "weather": "Extremely hot, 95-105°F (35-40°C). Low humidity. AT&T Stadium has AC and retractable roof.",
        "localTips": ["The stadium is climate-controlled — you'll be comfortable inside", "BBQ is king here — try Pecan Lodge or Hard Eight BBQ", "There's no Uber surge pricing cap in Texas — book early or share rides", "Visit the Fort Worth Stockyards for a Texas cultural experience", "Tex-Mex in Dallas is world-class — try Mi Cocina or Torchy's Tacos"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Medical City Arlington", "embassy": "Dallas has consulates for several countries"},
        "fanExperience": "Everything is bigger in Texas — including the stadium's massive video board. The BBQ tailgate culture around AT&T Stadium is legendary."
    },
    {
        "_id": "houston", "name": "Houston", "state": "TX", "country": "USA",
        "timezone": "America/Chicago", "currency": "USD", "language": "English/Spanish",
        "safety": ["Extremely hot and humid — heat stroke is a genuine concern", "Flooding can happen quickly — check weather before heading out", "Use rideshare at night in the NRG Park area"],
        "weather": "Hot and extremely humid, 90-95°F (32-35°C) with 70-80% humidity. Afternoon thunderstorms common.",
        "localTips": ["NRG Stadium has excellent AC — bring a light layer for inside", "Houston has the best Vietnamese food in the US — visit Midtown for pho", "The METRORail goes directly to NRG Park", "Visit NASA Space Center if you have a day off", "Houston's food scene is incredibly diverse — try Underbelly or Killen's BBQ"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Houston Methodist Hospital", "embassy": "Houston has a large consular district"},
        "fanExperience": "Houston's massive international community means every match feels like a home game for someone. Incredible food diversity around the stadium."
    },
    {
        "_id": "atlanta", "name": "Atlanta", "state": "GA", "country": "USA",
        "timezone": "America/New_York", "currency": "USD", "language": "English",
        "safety": ["Downtown is safe during events but quieter streets can be sketchy at night", "MARTA is safe and efficient — use it", "Stay hydrated — humidity is brutal"],
        "weather": "Hot and humid, 85-95°F (29-35°C). Mercedes-Benz Stadium is fully enclosed and climate-controlled.",
        "localTips": ["MARTA drops you right at the stadium — don't drive", "Mercedes-Benz has the cheapest concessions in pro sports — $2 hot dogs, $5 beers", "Visit the Georgia Aquarium or World of Coca-Cola nearby", "Ponce City Market is a great food hall 15 min from the stadium", "Peach cobbler and fried chicken are local staples"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Grady Memorial Hospital", "embassy": "Atlanta has consulates in Midtown"},
        "fanExperience": "Atlanta's soccer culture is among the strongest in the US. The supporter section at Mercedes-Benz Stadium is world-famous for its energy."
    },
    {
        "_id": "philadelphia", "name": "Philadelphia", "state": "PA", "country": "USA",
        "timezone": "America/New_York", "currency": "USD", "language": "English",
        "safety": ["The Sports Complex area is safe on game days", "Center City is walkable and well-lit", "Avoid North Philadelphia after dark"],
        "weather": "Hot and humid, 85-95°F (29-35°C). Open-air stadium — bring sunscreen and a hat.",
        "localTips": ["Get a real Philly cheesesteak — Pat's King of Steaks or Jim's on South St", "SEPTA Broad Street Line goes directly to the stadium", "Visit Reading Terminal Market for amazing local food", "Philly fans are passionate — embrace it", "The Liberty Bell and Independence Hall are free to visit"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Thomas Jefferson University Hospital", "embassy": "Philadelphia has limited consular presence — nearest major hub is NYC or DC"},
        "fanExperience": "Philly fans bring an unmatched intensity. The tailgate scene in the Sports Complex parking lots is a party unto itself."
    },
    {
        "_id": "seattle", "name": "Seattle", "state": "WA", "country": "USA",
        "timezone": "America/Los_Angeles", "currency": "USD", "language": "English",
        "safety": ["Pioneer Square can be rough at night", "Capitol Hill and Pike Place are safe and vibrant", "Downtown is walkable but hilly — wear comfortable shoes"],
        "weather": "Mild and pleasant, 70-80°F (21-27°C). Rare summer rain. The nicest weather Seattle gets all year.",
        "localTips": ["Lumen Field is downtown — walk from most hotels", "Seattle summers are gorgeous — enjoy it, locals wait all year for this", "Pike Place Market for fresh seafood and the original Starbucks", "Try Dick's Drive-In for a local burger experience", "The Link Light Rail goes directly to the stadium from the airport"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Harborview Medical Center", "embassy": "Seattle has consulates for several Asian and European countries"},
        "fanExperience": "The Sounders have built a world-class soccer culture in Seattle. Lumen Field is known as one of the loudest stadiums in America."
    },
    {
        "_id": "miami-gardens", "name": "Miami Gardens / Miami", "state": "FL", "country": "USA",
        "timezone": "America/New_York", "currency": "USD", "language": "English/Spanish",
        "safety": ["Miami Gardens can be rough outside of match day — stay near the stadium or in tourist areas", "South Beach and Brickell are safe and vibrant", "Use rideshare at night"],
        "weather": "Hot and humid, 85-95°F (29-35°C). Daily afternoon thunderstorms in summer. They usually pass in 30 min.",
        "localTips": ["Hard Rock Stadium is 30 min from South Beach — plan transport", "Cuban coffee (colada) is a must — try Versailles Restaurant on Calle Ocho", "The stadium's canopy provides shade but it's still outdoors — dress light", "Miami's nightlife starts at midnight — pace yourself", "Calle Ocho in Little Havana is essential for Latin American culture"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Jackson Memorial Hospital", "embassy": "Miami has consulates for virtually every Latin American country"},
        "fanExperience": "Miami's Latin culture makes this the most authentically international World Cup city in the US. Every match feels like a carnival."
    },
    {
        "_id": "foxborough", "name": "Foxborough / Boston", "state": "MA", "country": "USA",
        "timezone": "America/New_York", "currency": "USD", "language": "English",
        "safety": ["Foxborough is a small town — very safe", "Boston is generally safe — avoid certain parts of Dorchester and Roxbury at night", "Game day traffic is intense — leave VERY early"],
        "weather": "Warm, 75-85°F (24-29°C). Pleasant summer weather. Can cool down in the evenings to 65°F.",
        "localTips": ["Take the commuter rail — it runs special match-day service to Foxboro", "Foxborough has almost no restaurants — eat in Boston before heading out", "Boston's seafood is legendary — try Neptune Oyster or Legal Sea Foods", "Walk the Freedom Trail for American history", "Boston is a college town — vibrant pub scene in Cambridge and Back Bay"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Norwood Hospital", "embassy": "Boston has consulates for several European and Asian countries"},
        "fanExperience": "New England's passion for sports extends to soccer. The tailgate parking lot experience at Gillette is a tradition."
    },
    {
        "_id": "kansas-city", "name": "Kansas City", "state": "MO", "country": "USA",
        "timezone": "America/Chicago", "currency": "USD", "language": "English",
        "safety": ["The stadium area is safe on match days", "Power & Light District downtown is lively and safe", "Avoid east KC at night"],
        "weather": "Hot, 85-95°F (29-35°C). Can be humid. Occasional summer thunderstorms.",
        "localTips": ["KC BBQ is the best in America — try Joe's Kansas City, Q39, or Gates BBQ", "Arrowhead fans are incredibly passionate — the stadium holds the record for loudest crowd noise", "The stadium is in a sports complex with shared parking with Kauffman Stadium", "Power & Light District is the best nightlife area", "KC is affordable — hotel and food prices are lower than coastal cities"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Research Medical Center", "embassy": "Limited consular presence — nearest hubs are Chicago or Dallas"},
        "fanExperience": "Arrowhead Stadium is legendary for its noise. KC's BBQ tailgate culture is unmatched — some fans set up smokers at 7 AM."
    },
    {
        "_id": "santa-clara", "name": "Santa Clara / San Francisco Bay Area", "state": "CA", "country": "USA",
        "timezone": "America/Los_Angeles", "currency": "USD", "language": "English",
        "safety": ["Santa Clara is a safe suburban area", "San Francisco's Tenderloin and parts of SOMA should be avoided at night", "Car break-ins are common in SF — don't leave valuables visible"],
        "weather": "Warm and dry, 80-90°F (27-32°C) in Santa Clara. San Francisco is cooler at 65-70°F. Dress in layers.",
        "localTips": ["Levi's Stadium is in Santa Clara — 45 min from San Francisco", "The west side of the stadium gets brutal afternoon sun — sit on the east side if possible", "VTA Light Rail goes directly to the stadium", "Visit San Francisco for food — Mission District for burritos, Fisherman's Wharf for seafood", "Napa Valley wine country is a 1-hour drive north"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Kaiser Permanente Santa Clara", "embassy": "SF has consulates for 50+ countries"},
        "fanExperience": "Silicon Valley's tech culture meets world football. Expect a diverse, international crowd from the Bay Area's global community."
    },
    {
        "_id": "mexico-city", "name": "Mexico City", "state": "CDMX", "country": "Mexico",
        "timezone": "America/Mexico_City", "currency": "MXN", "language": "Spanish",
        "safety": ["Use Uber/DiDi instead of street taxis", "Avoid showing expensive jewelry or electronics in public", "Stick to well-known neighborhoods like Roma, Condesa, Polanco, and Centro", "Don't drink tap water — buy bottled"],
        "weather": "Mild, 70-80°F (21-27°C). Rainy season — afternoon showers almost daily but they clear quickly. Altitude: 7,350 ft — take it easy the first day.",
        "localTips": ["Altitude sickness is real at 7,350 ft — rest on arrival, drink lots of water, avoid alcohol the first day", "Street tacos are incredible and cheap — try tacos al pastor", "The Metro is extensive and cheap (5 MXN) but crowded", "Visit the Zócalo, Frida Kahlo Museum, and Chapultepec Castle", "Estadio Azteca is historic — two World Cup finals played here (1970, 1986)"],
        "emergencyContacts": {"police": "911", "ambulance": "065", "nearestHospital": "Hospital General de México", "embassy": "Most countries have embassies in Mexico City — check your government's website"},
        "fanExperience": "The most passionate football city in North America. Estadio Azteca's atmosphere is legendary — where Maradona scored the 'Hand of God' and 'Goal of the Century' in 1986."
    },
    {
        "_id": "guadalajara", "name": "Guadalajara", "state": "Jalisco", "country": "Mexico",
        "timezone": "America/Mexico_City", "currency": "MXN", "language": "Spanish",
        "safety": ["Tourist areas (Centro, Tlaquepaque, Zapopan) are generally safe", "Use Uber/DiDi at night", "Don't drink tap water"],
        "weather": "Warm, 80-90°F (27-32°C). Rainy season with afternoon thunderstorms. Evenings are pleasant.",
        "localTips": ["Guadalajara is the birthplace of tequila and mariachi — visit Tequila town (1 hour away)", "Try birria (spiced stew) — it's a local specialty", "Tlaquepaque is a beautiful artisan town for shopping", "The stadium is in Zapopan — 20 min from Centro by Uber", "Guadalajara is more affordable than Mexico City"],
        "emergencyContacts": {"police": "911", "ambulance": "065", "nearestHospital": "Hospital Civil de Guadalajara", "embassy": "US Consulate is in Guadalajara — other countries check Mexico City"},
        "fanExperience": "Jalisco's love for fútbol is deep. The atmosphere at Estadio Akron is electric, and the post-match celebrations spill into Guadalajara's vibrant nightlife."
    },
    {
        "_id": "monterrey", "name": "Monterrey", "state": "Nuevo León", "country": "Mexico",
        "timezone": "America/Monterrey", "currency": "MXN", "language": "Spanish",
        "safety": ["Tourist and business areas (San Pedro, Centro, Barrio Antiguo) are safe", "Use Uber/DiDi — avoid street taxis", "Don't venture into rural outskirts"],
        "weather": "Very hot, 90-100°F (32-38°C). Dry heat. Mountains provide dramatic backdrop but trap heat.",
        "localTips": ["Monterrey is Mexico's wealthiest city — modern and business-oriented", "Try cabrito (roasted goat) — the local delicacy", "Visit Fundidora Park — a beautiful urban park near the city center", "Estadio BBVA is one of the newest and most modern stadiums in Mexico", "San Pedro Garza García has upscale dining and shopping"],
        "emergencyContacts": {"police": "911", "ambulance": "065", "nearestHospital": "Hospital Universitario", "embassy": "US Consulate in Monterrey — other countries check Mexico City"},
        "fanExperience": "Monterrey's Rayados and Tigres have one of the fiercest rivalries in Mexican football. The passion carries over to World Cup matches."
    },
    {
        "_id": "toronto", "name": "Toronto", "state": "ON", "country": "Canada",
        "timezone": "America/Toronto", "currency": "CAD", "language": "English/French",
        "safety": ["Toronto is one of the safest major cities in North America", "The Entertainment District and waterfront are very safe", "Use TTC (transit) or rideshare — avoid driving downtown"],
        "weather": "Warm, 75-85°F (24-29°C). Pleasant summer weather. Occasional humidity and thunderstorms.",
        "localTips": ["BMO Field is on the waterfront — beautiful location", "Toronto is the most multicultural city in the world — food from every country", "Visit Kensington Market for eclectic food and shops", "The CN Tower observation deck gives amazing city views", "St. Lawrence Market is consistently rated one of the world's best food markets"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "St. Michael's Hospital", "embassy": "Most countries have embassies or consulates in Toronto"},
        "fanExperience": "Toronto FC fans created a strong supporter culture at BMO Field. The city's multiculturalism means fans from every qualifying nation will have a community here."
    },
    {
        "_id": "vancouver", "name": "Vancouver", "state": "BC", "country": "Canada",
        "timezone": "America/Vancouver", "currency": "CAD", "language": "English",
        "safety": ["Downtown and tourist areas are very safe", "East Hastings Street has visible homelessness — avoid at night", "Vancouver is generally one of the safest cities in the world"],
        "weather": "Mild and pleasant, 70-75°F (21-24°C). Driest time of year. Mountains and ocean create a stunning backdrop.",
        "localTips": ["BC Place is downtown — walk from most hotels", "Vancouver's sushi is the best outside Japan", "Take the SeaBus to North Vancouver for Grouse Mountain and Capilano Suspension Bridge", "Stanley Park is a must-visit — cycling the seawall is iconic", "Granville Island has an excellent public market"],
        "emergencyContacts": {"police": "911", "ambulance": "911", "nearestHospital": "Vancouver General Hospital", "embassy": "Vancouver has consulates for major countries"},
        "fanExperience": "Vancouver hosted the 2010 Winter Olympics and knows how to throw a party. The Whitecaps' supporter culture is growing, and BC Place's retractable roof makes weather a non-issue."
    }
]
