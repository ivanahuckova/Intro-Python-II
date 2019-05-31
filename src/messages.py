# Messages
hello = f"\n====================================================================\n         🌏   Hello and welcome to TRAVEL AROUND WESTEROS\n====================================================================\n"


def goodbye(c):
    print(
        f"""\n====================================================================
     YOU HAVE DECIDED TO STAY AT: {c.name.upper()} {c.emoji}. GREAT CHOICE! 👋 
====================================================================\n""")


where_to_go = f"\n❔   Would you like to stay (use q) or go somewhere else? Use n/s/w/e for navigation: "


def offer_items(f, s):
    print(
        f"""You've been offered  {f.upper()}  and  {s.upper()}. 
You can choose to not take anything (input no) or choode 1 item. 
Also, remember, you can allways carry only 3 things at the time.
""")
