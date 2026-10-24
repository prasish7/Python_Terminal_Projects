
horoscope_signs = {
    "Aries": "March 21 - April 19",
    "Taurus": "April 20 - May 20",
    "Gemini": "May 21 - June 20",
    "Cancer": "June 21 - July 22",
    "Leo": "July 23 - August 22",
    "Virgo": "August 23 - September 22",
    "Libra": "September 23 - October 22",
    "Scorpio": "October 23 - November 21",
    "Sagittarius": "November 22 - December 21",
    "Capricorn": "December 22 - January 19",
    "Aquarius": "January 20 - February 18",
    "Pisces": "February 19 - March 20"
}
messages = {
    "Aries": "Today is a great day to take initiative and lead the way.",   
    "Taurus": "Patience will bring you rewards in unexpected ways.",
    "Gemini": "Communication is key; reach out to someone you care about.",
    "Cancer": "Trust your intuition; it will guide you through challenges.",
    "Leo": "Your confidence will inspire those around you.",
    "Virgo": "Attention to detail will help you achieve your goals.",
    "Libra": "Seek balance in your relationships and work life.",
    "Scorpio": "Embrace change; it will lead to personal growth.",
    "Sagittarius": "Adventure awaits; be open to new experiences.",
    "Capricorn": "Hard work will pay off; stay focused on your ambitions.",
    "Aquarius": "Innovative ideas will lead to exciting opportunities.",
    "Pisces": "Creativity will flow; express yourself freely."
}

def get_horoscope(sign):
    sign = sign.capitalize()
    if sign in horoscope_signs:
        return f"{sign} ({horoscope_signs[sign]}): {messages[sign]}"
    else:
        return "Invalid horoscope sign. Please enter a valid sign."


if __name__ == "__main__":
    user_sign = input("Enter your horoscope sign: ")
    print(get_horoscope(user_sign))