import os

# ─── FULL CASE DATA (all 21 entries from your document) ──────────────
case_data = [
    {
        "id": "terry-v-ohio",
        "title": "Terry v. Ohio",
        "citation": "392 U.S. 1 (1968)",
        "summary": 'A person can be detained for "reasonable suspicion" based on articulable facts. That reasonable suspicion must be based on officer experience and knowledge but must be "articulable" — facts that can be described on paper. If you cannot describe those facts so that someone can read and understand them, it does not exist.',
        "impact": 'Establishes the "Terry stop" — officers may briefly detain and question individuals based on reasonable suspicion of criminal activity, without probable cause for arrest. The suspicion must be specific and articulable, not a mere hunch.',
        "source": "SCOTUS, 392 U.S. 1 (1968)"
    },
    {
        "id": "chimel-v-california",
        "title": "Chimel v. California",
        "citation": "395 U.S. 752 (1969)",
        "summary": 'When a person is arrested in his residence, a search of the immediate "wingspan" area — where he could hide weapons or evidence — can be searched without a warrant. No other areas of the home may be searched.',
        "impact": 'Defines the scope of a warrantless search incident to arrest inside a home. Officers may only search the area within the arrestee\'s immediate reach (the "wingspan") for officer safety or to prevent destruction of evidence.',
        "source": "SCOTUS, 395 U.S. 752 (1969)"
    },
    {
        "id": "arizona-v-gant",
        "title": "Arizona v. Gant",
        "citation": "556 U.S. 332 (2009)",
        "summary": 'When an arrest is made in a vehicle, a wingspan search is not allowed unless it is for evidence related to the reason for arrest. Example: arrest for assault with a deadly weapon → can search for that weapon. Arrest for no driver\'s license → no wingspan search justified. This does not prevent an inventory search (South Dakota v. Opperman) or probable cause search (Carroll v. US).',
        "impact": 'Limits vehicle searches incident to arrest. Officers may only search the passenger compartment if the arrestee is unsecured and within reaching distance, or if they have reason to believe the vehicle contains evidence related to the crime of arrest.',
        "source": "SCOTUS, 556 U.S. 332 (2009)"
    },
    {
        "id": "carroll-v-us",
        "title": "Carroll v. United States",
        "citation": "267 U.S. 132 (1925)",
        "summary": 'If probable cause exists that evidence or contraband is in a moveable vehicle, a warrant is not needed to search any area where that evidence may be found. If the vehicle is not moveable (e.g., in a shop, disabled in a front yard on blocks), the automobile exception does not apply and a warrant is required. Carroll applies on traffic stops where the person can drive away — no time for a warrant.',
        "impact": 'Establishes the "automobile exception" to the warrant requirement. Because vehicles are mobile and there is a reduced expectation of privacy, officers may search them without a warrant if they have probable cause to believe contraband or evidence is inside.',
        "source": "SCOTUS, 267 U.S. 132 (1925)"
    },
    {
        "id": "whren-v-us",
        "title": "Whren v. United States",
        "citation": "517 U.S. 806 (1996)",
        "summary": 'In Whren, narcotics officers saw a suspicious vehicle and pulled it over for a traffic violation, leading to a drug conviction. Whren argued the stop was a pretext for drug investigation. A unanimous SCOTUS held that a temporary detention of a motorist is lawful if based on probable cause, even if the stop would not have been made absent some other law enforcement objective.',
        "impact": 'Establishes that pretextual stops are constitutional as long as there is probable cause for a traffic violation. Officers may use a traffic stop as a basis for further investigation, provided they have PC for the initial stop.',
        "source": "SCOTUS, 517 U.S. 806 (1996)"
    },
    {
        "id": "wardlow-v-illinois",
        "title": "Wardlow v. Illinois",
        "citation": "528 U.S. 119 (2000)",
        "summary": 'The SCOTUS ruled that "headlong flight" from officers is reasonable suspicion under Terry v. Ohio. Officers converged on a known drug area; Wardlow saw them and immediately ran. Officers chased, detained him, and found a gun. The Court ruled that seeing police and immediately fleeing is suspicious and justifies a Terry stop. The Court did not say fleeing is a crime in itself.',
        "impact": 'Flight from officers in a high-crime area can contribute to reasonable suspicion for a stop. Officers should rely on state law (e.g., TX Penal Code) for evading detention charges, but flight alone — especially in a known drug area — can justify a brief investigative detention.',
        "source": "SCOTUS, 528 U.S. 119 (2000)"
    },
    {
        "id": "florida-v-jl",
        "title": "Florida v. J. L.",
        "citation": "529 U.S. 266 (2000)",
        "summary": 'Generally, officers may not even detain a person based solely on an anonymous tip. Example: a call about a person dealing drugs on a corner with a good description, but the reporter is not identified. If the information cannot be independently verified (not merely the description), a detention is unlawful. In J.L., officers had a great description of a guy with a pistol at a specific location. They stopped him and found an illegal firearm. SCOTUS threw out the case because officers had no way of knowing the tip was valid by independent observation before the illegal detention and search.',
        "impact": 'An anonymous tip alone, without independent corroboration, does not provide reasonable suspicion for a stop. Officers must observe some corroborating detail (e.g., a bulge, furtive movements) before detaining. There is no "gun exception" to the 4th Amendment.',
        "source": "SCOTUS, 529 U.S. 266 (2000)"
    },
    {
        "id": "ny-v-quarles",
        "title": "New York v. Quarles",
        "citation": "467 U.S. 649 (1984)",
        "summary": 'Yes, in a very limited circumstance. If the public is in immediate danger AND it is a dynamic situation, asking a question to potentially save a life is allowed. Officers spotted Quarles, a rape suspect. He fled into a store and was arrested. A frisk found an empty shoulder holster. The officer asked where the gun was; Quarles nodded and said "over there." The gun was found. SCOTUS upheld the question as an accomplice might have found the gun and threatened officers or an innocent person (like a child) might have been in danger.',
        "impact": 'Creates a "public safety" exception to Miranda. Officers may ask questions about immediate safety threats without first giving Miranda warnings, but this exception is narrow and applies only to urgent, dynamic situations where there is a risk to public or officer safety.',
        "source": "SCOTUS, 467 U.S. 649 (1984)"
    },
    {
        "id": "kaupp-v-texas",
        "title": "Kaupp v. Texas",
        "citation": "538 U.S. 626 (2003)",
        "summary": 'Telling people "magic words" like "you are not in custody" or "you are being handcuffed for your safety" does not negate Miranda. The entire circumstances dictate whether someone is in custody. Kaupp was a murder suspect. Deputies went to his home early morning, woke him, said "we need to talk," and brought him to the station in handcuffs (policy for safety). Once there, he was read Miranda and confessed. A unanimous SCOTUS threw out the confession. The consent was not freely given; being awakened and told to talk is intimidating.',
        "impact": 'Officers cannot avoid Miranda by simply saying someone is not in custody. Courts look at the totality of circumstances from the perspective of a reasonable person. Handcuffing, transporting to the station, or waking someone at home can all indicate custody, regardless of the officer\'s words.',
        "source": "SCOTUS, 538 U.S. 626 (2003)"
    },
    {
        "id": "muehler-v-mena",
        "title": "Muehler v. Mena",
        "citation": "544 U.S. 93 (2005)",
        "summary": 'Unlike Kaupp, police in Muehler had a search warrant. They entered a home with gang members known to be present and handcuffed occupants for safety. Mena contested the detention and questioning as a 4th Amendment violation. A unanimous SCOTUS sided with police, allowing detention of occupants for safety under such a warrant without individual PC or RS on each person.',
        "impact": 'When executing a search warrant, officers may detain occupants of the premises for safety reasons without needing individualized reasonable suspicion or probable cause. This is based on the "Michigan v. Summers" principle that officers have an interest in preventing flight and ensuring safety during a warrant execution.',
        "source": "SCOTUS, 544 U.S. 93 (2005)"
    },
    {
        "id": "horton-v-california",
        "title": "Horton v. California",
        "citation": "496 U.S. 128 (1990)",
        "summary": 'Plain view does not simply mean you can see something. It has three requirements: (1) the officer is lawfully present at the location, (2) the officer has a lawful right to access the item, and (3) it must be "immediately apparent" that the item is contraband. The officer cannot move or manipulate the item for it to fall under plain view. Example: seeing a television and moving it to see the serial number — if it comes back stolen, that is an illegal search.',
        "impact": 'Plain view seizures are only lawful if the incriminating nature of the item is immediately apparent without moving or manipulating it. Officers cannot conduct a warrantless search by moving items to check for evidence; the evidence must be readily observable from a lawful vantage point.',
        "source": "SCOTUS, 496 U.S. 128 (1990)"
    },
    {
        "id": "minnesota-v-dickerson",
        "title": "Minnesota v. Dickerson",
        "citation": "508 U.S. 366 (1993)",
        "summary": 'A unanimous SCOTUS ruled that if an officer lawfully pats down a person and discovers contraband, it can be seized. However, the officer lost the case but set a precedent. Just as with plain view, the officer cannot manipulate the item — it must be "immediately apparent" on merely touching the item that it is contraband. Example: feeling a soft baggie while patting for weapons — you cannot roll it around to determine what it is. If you can touch it with a flat hand and immediately know it\'s contraband, it is lawful to remove it.',
        "impact": 'Establishes the "plain feel" doctrine. During a lawful Terry frisk, officers may seize contraband if its incriminating nature is immediately apparent through touch. Manipulation beyond a light pat-down to identify an object is not allowed and constitutes an unlawful search.',
        "source": "SCOTUS, 508 U.S. 366 (1993)"
    },
    {
        "id": "pennsylvania-v-mimms",
        "title": "Pennsylvania v. Mimms",
        "citation": "434 U.S. 106 (1977)",
        "summary": 'Yes. The SCOTUS ruled that for officer safety, there is no need to articulate reasonable suspicion to remove a driver from a vehicle. To control a scene, you can order a driver out of the vehicle.',
        "impact": 'Officers may order a driver out of a vehicle during a traffic stop as a matter of routine safety, without any additional justification. This is a minimal intrusion that is outweighed by officer safety concerns.',
        "source": "SCOTUS, 434 U.S. 106 (1977)"
    },
    {
        "id": "maryland-v-wilson",
        "title": "Maryland v. Wilson",
        "citation": "519 U.S. 408 (1997)",
        "summary": 'Yes, for the same reasons given in Mimms. The SCOTUS extended the rule to passengers, allowing officers to order passengers out of a vehicle during a traffic stop for officer safety.',
        "impact": 'Officers may order passengers out of a vehicle during a traffic stop without needing additional reasonable suspicion. This is a safety measure and applies to all occupants of the vehicle.',
        "source": "SCOTUS, 519 U.S. 408 (1997)"
    },
    {
        "id": "katz-v-us",
        "title": "Katz v. United States",
        "citation": "389 U.S. 347 (1967)",
        "summary": 'Yes. The 4th Amendment protects people, not places, according to the SCOTUS in a 7-1 ruling. This includes not only physical entry like an officer reaching into an area but any intrusion including electronic transmission such as a phone recording, even in a public place like a public phone booth. A person\'s right to privacy goes with him.',
        "impact": 'Establishes the "reasonable expectation of privacy" test. The 4th Amendment protects people, not places. Officers must obtain a warrant before conducting electronic surveillance or searching areas where a person has a legitimate expectation of privacy, even in public spaces.',
        "source": "SCOTUS, 389 U.S. 347 (1967)"
    },
    {
        "id": "riley-v-california",
        "title": "Riley v. California",
        "citation": "573 U.S. 373 (2014)",
        "summary": 'No. A unanimous SCOTUS ruled that a cell phone is a personal record similar to a home computer and no longer holds only phone calls. It requires a search warrant or consent to search a phone.',
        "impact": 'Officers generally cannot search a cell phone incident to arrest without a warrant. The vast amount of personal data on a phone requires a warrant, unless exigent circumstances exist (e.g., destruction of evidence, imminent danger).',
        "source": "SCOTUS, 573 U.S. 373 (2014)"
    },
    {
        "id": "brigham-city-v-stuart",
        "title": "Brigham City v. Stuart",
        "citation": "547 U.S. 398 (2006)",
        "summary": 'Yes, says a unanimous SCOTUS, if it is with probable cause to stop an assault with "serious injuries" or the threat of those injuries. Officers may enter a home without a warrant in an emergency situation to prevent violence or injury.',
        "impact": 'The "emergency aid" exception allows warrantless entry into a home when officers have probable cause to believe someone is seriously injured or imminently threatened with serious injury. This is a public safety exception to the warrant requirement.',
        "source": "SCOTUS, 547 U.S. 398 (2006)"
    },
    {
        "id": "mincey-v-arizona",
        "title": "Mincey v. Arizona",
        "citation": "437 U.S. 385 (1978)",
        "summary": 'There is no homicide exception to the search warrant requirement. Due to the seriousness of the offense, officers might believe a warrant is not needed, but that is incorrect. A right to privacy does not go away with a more serious accusation. At a violent crime scene, officers have the right to check for more victims or a suspect that may be a danger — meaning you can search anywhere a person might be, but not look into other areas. The scene must then be secured and a warrant obtained if there is an expectation of privacy.',
        "impact": 'There is no "homicide scene exception" to the warrant requirement. Officers may conduct a warrantless search only to the extent necessary to secure the scene and check for victims or suspects. Once the scene is secure, a warrant is required to search further.',
        "source": "SCOTUS, 437 U.S. 385 (1978)"
    },
    {
        "id": "cady-v-dombrowski",
        "title": "Cady v. Dombrowski",
        "citation": "413 U.S. 433 (1973)",
        "summary": 'The Community Caretaker doctrine allows officers the limited ability to have contraband admissible as evidence without probable cause or consent. If an officer is not providing a law enforcement function but is merely checking on the welfare of a person or situation, contraband discovered in plain view may be evidence. In Dombrowski, police investigated an accident involving an off-duty officer. They entered the car at the wrecker yard to secure a gun for public safety and found bloody clothing that led to a murder charge.',
        "impact": 'Officers may act in a "community caretaker" role — checking on welfare, securing property, etc. — without needing probable cause. Contraband discovered in plain view during such a non-law-enforcement function may be admissible. This is limited and does not apply to investigative detentions.',
        "source": "SCOTUS, 413 U.S. 433 (1973)"
    },
    {
        "id": "brown-v-texas",
        "title": "Brown v. Texas",
        "citation": "443 U.S. 47 (1979)",
        "summary": 'Reaffirms Terry v. Ohio and the requirement to have at least reasonable suspicion to force a detention. A consent encounter requires the officer, using no force or threats, to question whether a person wishes to talk. If you tell a person "Come here," "Stop," "Let me see your hands," etc., you have likely detained them. For a consent interaction, phrase it like "Do you mind speaking to me?" or "Do you mind me looking in your pockets?"',
        "impact": 'Officers must have reasonable suspicion to detain someone. A "consensual encounter" is only valid if a reasonable person would feel free to leave or refuse. Commands, forceful tones, or showing authority can turn an encounter into a detention requiring RS.',
        "source": "SCOTUS, 443 U.S. 47 (1979)"
    },
    {
        "id": "res-gestae",
        "title": "Res Gestae (Doctrine)",
        "citation": "Hearsay Exception",
        "summary": 'Res Gestae is an exception to the hearsay rule. Generally, overheard statements are not allowed into evidence at trial — the person who made the statement must testify. Res Gestae, like a confession, is allowed under certain circumstances. A Res Gestae statement is spontaneous — like blurting out words after an incident or in response to a general question, not as a result of meditation. Example: a person in a crowd shouts "That man running in the red shirt just robbed the bank!" or "I shot him!"',
        "impact": 'Officers may document spontaneous statements made by witnesses or suspects in the heat of the moment, as they may be admissible under the Res Gestae exception. If an officer is questioning a specific person about a particular incident, the response is not Res Gestae and is governed by rules of oral/written statements or confessions.',
        "source": "Common Law Doctrine — Hearsay Exception"
    }
]

# ─── HTML TEMPLATE for individual case pages ──────────────────────
TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} – Case Law</title>
    <link rel="icon" href="../department-badge.png" type="image/png">
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.7;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        header {{
            background-color: #1a3a6e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            flex-wrap: wrap;
        }}
        .badge-left {{
            width: 125px;
            height: 125px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .badge-left img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: block;
        }}
        .header-text {{
            flex: 1;
            text-align: center;
        }}
        .header-text h1 {{
            margin: 0;
            font-size: 28px;
        }}
        .subtitle {{
            margin-top: 5px;
            font-size: 16px;
            opacity: 0.9;
        }}
        .badge-right {{
            width: 100px;
            height: 100px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .badge-right img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: block;
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            color: #1a3a6e;
            text-decoration: none;
            font-weight: 600;
            padding: 8px 16px;
            background: white;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
            transition: background 0.2s;
        }}
        .back-link:hover {{
            background: #e9f0fd;
            text-decoration: underline;
        }}
        .back-link::before {{
            content: '← ';
        }}
        .case-card {{
            background: white;
            border-radius: 5px;
            padding: 28px 30px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            border-left: 6px solid #1a3a6e;
        }}
        .case-card h1 {{
            color: #1a3a6e;
            font-size: 28px;
            margin-bottom: 4px;
        }}
        .case-card .citation {{
            font-size: 16px;
            color: #777;
            font-weight: 500;
            background: #f0f2f5;
            display: inline-block;
            padding: 2px 16px;
            border-radius: 16px;
            margin-bottom: 20px;
        }}
        .case-card .section {{
            margin-top: 20px;
        }}
        .case-card .section strong {{
            color: #1a3a6e;
            display: block;
            font-size: 17px;
            margin-bottom: 4px;
        }}
        .case-card .section .impact-box {{
            padding: 14px 18px;
            background: #e9f0fd;
            border-radius: 4px;
            border-left: 3px solid #1a3a6e;
            margin-top: 6px;
        }}
        .case-card .source {{
            margin-top: 24px;
            padding-top: 14px;
            border-top: 1px solid #e8ecf1;
            font-size: 15px;
            color: #555;
        }}
        .case-card .source strong {{
            color: #1a3a6e;
        }}
        footer {{
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #777;
            padding: 16px 0;
            border-top: 1px solid #e0e0e0;
        }}
        @media (max-width: 700px) {{
            body {{ padding: 12px; }}
            header {{ padding: 15px; justify-content: center; }}
            .badge-left {{ width: 50px; height: 50px; }}
            .badge-right {{ width: 40px; height: 40px; }}
            .header-text h1 {{ font-size: 20px; }}
            .subtitle {{ font-size: 11px; }}
            .case-card {{ padding: 18px 16px; }}
            .case-card h1 {{ font-size: 22px; }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="badge-left">
            <img src="../officer-badge.png" alt="Officer Badge"
            onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Ccircle cx=%2250%22 cy=%2250%22 r=%2245%22 fill=%22%23ffcd3c%22/%3E%3Ctext x=%2250%22 y=%2268%22 text-anchor=%22middle%22 fill=%22%231a3a6e%22 font-size=%2220%22 font-weight=%22bold%22%3EO%3C/text%3E%3C/svg%3E';">
        </div>
        <div class="header-text">
            <h1>Police Case Law Library</h1>
            <div class="subtitle">Individual case reference</div>
        </div>
        <div class="badge-right">
            <img src="../department-badge.png" alt="Police Department Badge"
            onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Ccircle cx=%2250%22 cy=%2250%22 r=%2245%22 fill=%22%231a3a6e%22/%3E%3Ctext x=%2250%22 y=%2268%22 text-anchor=%22middle%22 fill=%22white%22 font-size=%2216%22 font-weight=%22bold%22%3EPAPD%3C/text%3E%3C/svg%3E';">
        </div>
    </header>

    <a href="../index.html" class="back-link">← Back to Case Categories</a>

    <div class="case-card">
        <h1>{title}</h1>
        <div class="citation">{citation}</div>

        <div class="section">
            <strong>📘 Summary</strong>
            <p>{summary}</p>
        </div>

        <div class="section">
            <strong>⚖️ Impact on Law Enforcement</strong>
            <div class="impact-box">{impact}</div>
        </div>

        <div class="source">
            <strong>Source:</strong> {source}
        </div>
    </div>

    <footer>
        &copy; 2025 Port Arthur Police Department. All rights reserved.
    </footer>

</body>
</html>
'''


def main():
    os.makedirs("cases", exist_ok=True)

    for case in case_data:
        filename = f"cases/{case['id']}.html"
        content = TEMPLATE.format(
            title=case['title'],
            citation=case['citation'],
            summary=case['summary'],
            impact=case['impact'],
            source=case['source']
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Generated {filename}")

    print(f"\n🎉 All {len(case_data)} case files generated successfully in the 'cases/' folder.")


if __name__ == "__main__":
    main()