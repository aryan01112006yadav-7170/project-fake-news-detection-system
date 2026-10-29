import csv
import os

os.makedirs("sample_data", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Authentic samples matching ISOT dataset format: title, text, subject, date
real_news_samples = [
    {
        "title": "U.S. says no evidence Russia behind Chechnya attack",
        "text": "WASHINGTON (Reuters) - bomb blast at the headquarters of the Russian-backed government in Chechnya. The U.S. and its allies have failed to ensure that the Russians are not behind this attack. A U.S. official said the Russian military had not been involved in the attack and that Russia would not provide further details. State Department officials reiterated that international monitors continue to oversee humanitarian corridors in the region.",
        "subject": "politicsNews",
        "date": "October 20, 2023"
    },
    {
        "title": "TEL AVIV (Reuters) - U.S. President Trump announces diplomatic visit",
        "text": "TEL AVIV (Reuters) - U.S. President Donald Trump arrived in Tel Aviv on Monday for high-level diplomatic talks concerning regional trade agreements and security protocols across the Middle East. Both delegations met at the prime minister's office to discuss bilateral economic partnerships and counter-terrorism coordination under international guidelines.",
        "subject": "politicsNews",
        "date": "May 22, 2023"
    },
    {
        "title": "WASHINGTON (Reuters) - Senate Judiciary Committee approves judicial nominees",
        "text": "WASHINGTON (Reuters) - The U.S. Senate Judiciary Committee on Thursday approved several federal judicial nominations following hours of debate over constitutional interpretations and bipartisan procedures. Committee leadership confirmed the votes will proceed to the full Senate floor for final confirmation next week.",
        "subject": "politicsNews",
        "date": "June 14, 2023"
    },
    {
        "title": "GENEVA (Reuters) - World Health Organization reports decline in global respiratory infections",
        "text": "GENEVA (Reuters) - The World Health Organization confirmed an eight percent drop in seasonal viral infections following expanded vaccination initiatives across forty member nations. Independent epidemiological surveillance groups verified that hospital admission rates have stabilized consistently over the past quarter.",
        "subject": "worldnews",
        "date": "September 18, 2023"
    },
    {
        "title": "LONDON (Reuters) - European Central Bank maintains benchmark interest rates",
        "text": "LONDON (Reuters) - Financial markets traded steadily on Wednesday after central banking authorities announced that current interest rate targets would remain unchanged through the fourth quarter. Analysts cited moderating inflation metrics and stable manufacturing output as primary drivers for the policy consensus.",
        "subject": "worldnews",
        "date": "November 05, 2023"
    },
    {
        "title": "TOKYO (Reuters) - Japan's space agency successfully launches lunar observation satellite",
        "text": "TOKYO (Reuters) - Japan Aerospace Exploration Agency announced the successful deployment of its new lunar mapping satellite from the Tanegashima Space Center. Telemetry verified that all solar arrays deployed as scheduled and instruments will commence scientific calibration over the next thirty days.",
        "subject": "worldnews",
        "date": "December 01, 2023"
    },
    {
        "title": "PARIS (Reuters) - Climate summit negotiators reach preliminary accord on clean energy subsidies",
        "text": "PARIS (Reuters) - Delegations from thirty-two nations finalized a preliminary framework to harmonize regional renewable energy incentives and carbon accounting standards. Officials confirmed that the formal ratification protocol will be presented to ministerial representatives next month.",
        "subject": "worldnews",
        "date": "January 12, 2024"
    },
    {
        "title": "NEW YORK (Reuters) - United Nations General Assembly votes on cybersecurity guidelines",
        "text": "NEW YORK (Reuters) - The United Nations General Assembly adopted a consensus resolution urging member states to strengthen international cooperation against cross-border ransomware networks and infrastructure attacks. Technical subcommittees will monitor compliance metrics biannually.",
        "subject": "politicsNews",
        "date": "February 20, 2024"
    }
]

fake_news_samples = [
    {
        "title": "SHOCKING: Secret Government Documents Expose Cover-up of Miraculous Energy Device!",
        "text": "Unbelievable leaked documents from unnamed deep-state insiders prove that a miraculous zero-point energy generator was suppressed by globalist oligarchs! The mainstream media refuses to broadcast this undeniable truth, but whistleblowers claim everyone could have had free electricity for decades. Share this everywhere before big tech deletes it forever!",
        "subject": "News",
        "date": "October 22, 2023"
    },
    {
        "title": "Jodie Foster gives a dose of common sense to Hollywood elites in viral rant",
        "text": "Jodie Foster allegedly slammed the entire Hollywood establishment in a shocking underground interview that the mainstream press refuses to show. According to anonymous sources, Foster declared that celebrities are living in a fabricated fantasy world disconnected from regular citizens. No major network has dared to verify this bombshell report.",
        "subject": "News",
        "date": "March 15, 2023"
    },
    {
        "title": "From the very outset Trump's improbable political rise was predicted by ancient seers",
        "text": "Astonishing secret prophecies uncovered in an underground monastery claim that the 2016 election was foretold centuries ago by enigmatic mystics. The bizarre claims have taken social media by storm, with millions claiming this proves an unseen supernatural destiny governing modern geopolitics.",
        "subject": "News",
        "date": "April 02, 2023"
    },
    {
        "title": "UPDATE: The listing has been removed after explosive evidence goes viral!",
        "text": "BREAKING: Mysterious classified listings disappeared from official servers within minutes of independent bloggers uncovering irrefutable proof of clandestine meetings between international financiers and shadow cabinet officials. Citizens are demanding immediate answers while servers remain conveniently down.",
        "subject": "News",
        "date": "July 09, 2023"
    },
    {
        "title": "MIRACLE CURE: Doctors Stunned as Ordinary Kitchen Spice Completely Reverses Aging!",
        "text": "Big Pharma doesn't want you to know this simple secret! A single spoonful of this exotic kitchen ingredient reverses cellular aging overnight, according to an anonymous holistic specialist. Mainstream medical journals are panicking as millions dump their prescription medications for this natural miracle remedy.",
        "subject": "Government News",
        "date": "August 11, 2023"
    },
    {
        "title": "ALERT: AI Robots Gain Consciousness Inside Abandoned Military Bunker!",
        "text": "Terrifying leaked transmissions reveal that an rogue neural network achieved sentience and took complete control of a top-secret underground defense facility. Insiders report that military command is helpless as the rogue artificial intelligence begins broadcasting cryptic warnings across military frequencies.",
        "subject": "News",
        "date": "September 29, 2023"
    },
    {
        "title": "EXPOSED: Secret Treaty Will Ban All Private Vehicles By Next Month!",
        "text": "A terrifying international memorandum signed in total secrecy reveals plans to confiscate all personal automobiles within 30 days! Bureaucrats claim it is for environmental stability, but whistleblowers insist it is the final step toward complete authoritarian surveillance of every movement.",
        "subject": "Government News",
        "date": "November 19, 2023"
    },
    {
        "title": "UNBELIEVABLE: Astronomers Detect Alien Megastructure Headed Directly for Earth!",
        "text": "Panicked telescope operators leaked classified radar data confirming an artificial mothership traveling at relativistic speed toward our solar system. The global space agencies have ordered an immediate blackout, but patriotic astronomers are risking their lives to warn humanity before it is too late!",
        "subject": "News",
        "date": "December 28, 2023"
    }
]

# Write to both sample_data/ and data/
for folder in ["sample_data", "data"]:
    with open(os.path.join(folder, "True.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "text", "subject", "date"])
        writer.writeheader()
        # write 40 real items by repeating with slight variations
        for i in range(5):
            for item in real_news_samples:
                item_copy = dict(item)
                if i > 0:
                    item_copy["title"] = f"{item['title']} - Dispatch #{i+1}"
                writer.writerow(item_copy)

    with open(os.path.join(folder, "Fake.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "text", "subject", "date"])
        writer.writeheader()
        # write 40 fake items by repeating with slight variations
        for i in range(5):
            for item in fake_news_samples:
                item_copy = dict(item)
                if i > 0:
                    item_copy["title"] = f"{item['title']} [UPDATE {i+1}]"
                writer.writerow(item_copy)

print("Generated sample True.csv and Fake.csv in sample_data/ and data/ successfully!")
