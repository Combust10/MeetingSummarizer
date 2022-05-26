#pip install transformers[sentencepiece]
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk

#text = """ The Lightning Thief follows the story of young Percy Jackson, a troubled 12-year-old boy with a secret unknown even to himself. Diagnosed with dyslexia and ADHD, while being raised primarily by his mother, his life so far has not always been easy. Percy is repeatedly kicked out of school due to unexplainable events that aren’t really his fault. While on a sixth-grade field trip to a museum, Percy faces his strangest event yet. After an argument with a school bully, his math teacher, Mrs. Dodds, draws Percy aside to punish him. Mrs. Dodds suddenly transforms into a monster and attacks him. His favorite teacher, Mr. Brunner, rescues Percy by throwing him a ballpoint pen that changes into a sword. Although Percy defeats Mrs. Dodds, when he reunites with his other classmates, no one remembers her. In response, Percy acts out and is expelled from school. Percy overhears a conversation between Mr. Brunner and his friend Grover regarding Percy’s impending future, so he seeks answers from Grover on the bus ride home. After the bus breaks down, Percy and Grover notice three old women across the street knitting. One of the women cuts a string, which Percy and Grover discuss as signifying death. At home, Percy escapes his dreadful stepfather, whom he calls Smelly Gabe, by joining his mother, Sally, on a trip to their favorite beach where she originally met his birth father. Forceful winds and an unexpected visit from Grover lead Percy to reveal to his mother the incident that happened with Mrs. Dodds. After Percy finishes his story, Sally instructs Grover and Percy to get into the car where Percy notices Grover has hooves for feet and learns his friend is a satyr. Sally insists that Percy must go to a special camp for his safety. A monster chases after their car as they head in that direction, attacking Percy’s mother, which causes her to disappear into a golden light. Enraged, and fearing his mother’s death, Percy defeats the monster and obtains one of its horns as a souvenir. 
#Percy arrives at Camp Half-Blood and meets Mr. D, the god of wine, and Chiron, a centaur, formerly known as Mr. Brunner, Percy’s Latin teacher. Chiron and Grover explain to Percy that he is a half-blood, or a demi-god, meaning that he is half mortal and half god. Since his godly parent is unknown, Percy is assigned the cabin dedicated to Hermes. At camp, Percy meets Annabeth, the daughter of Athena; his cabin counselor Luke, the son of Hermes; and Clarisse, the daughter of Ares. An altercation with Clarisse allows Percy to discover his father is Poseidon, one of the “Big Three” gods. This revelation is cut short when a hellhound attacks Percy from the Fields of Punishment. Chiron protects everyone at the camp by sending Percy off on a special quest to save the world.  Percy’s Oracle reveals that Zeus has accused Poseidon of stealing his lightning bolt and requires Poseidon’s son to return it before the summer solstice. Chiron believes Hades actually stole the bolt to start a war between the gods. Percy chooses Grover and Annabeth to accompany him on his quest and together they head west to the entrance of the Underworld to confront Hades on the missing bolt. Along the way, the three will face several monsters before making it to Hades’ house. On one part of their journey, Percy and his friends fight the Furies, which causes the bus they are on to explode. After escaping into nearby woods, they come across a shop filled with many life-size statues. They meet Aunty Em, who Annabeth later identifies as Medusa. Percy defeats Medusa and sends her head to Olympus to show that he’s not a pawn in the gods’ game. Annabeth, Percy, and Grover take a train to Denver but stop at an Arch during a layover where Percy encounters the monsters Echidna and Chimera. He jumps off the Arch into the river to avoid dying and is met by a spirit who tells him to go to Santa Monica before going to the Underworld. In Denver, Percy, Annabeth, and Grover meet Ares, the god of war, who requests their help in retrieving his shield in exchange for information on Percy’s mother. Despite facing a trap placed by Hephaestus, Aphrodite’s husband, the three successfully grab the shield and return it to Ares who tells Percy that his mother is still alive. Ares gives the trio a backpack of supplies and safe transportation to Nevada. Percy and his friends continue west but lose track of time in a magical casino in Las Vegas, which leaves them only one more day to find and return the master bolt. Percy, Annabeth, and Grover arrive in Santa Monica where Percy receives three pearls from the same spirit who visited him in the river. The three search for directions to the Underworld and encounter a monster named Crusty. Percy defeats this monster and finds the address to an entrance to the Underworld. In the Underworld, Percy barters with Charon, a security officer, to let them in and tries to distract Cerberus, a three-headed security Rottweiler, but Annabeth is able to successfully command him. While on their way to Hades’ house, Grover’s flying shoes, on loan from Luke, pull him toward a pit Percy has dreamed uneasily about. Luckily, the shoes fall off before Grover reaches the pit. Finally, at the house, Hades accuses Percy of stealing his Helm of Darkness as well as the master bolt that surprisingly appears in the backpack Percy received from Ares. Hades reveals Percy’s mother to him in a golden light and says she will be returned once his helm is retrieved. Percy denies the allegations but after Hades threatens to kill his mother and unleash the dead back into the world, he agrees to find and return the helm. Percy, Grover, and Annabeth escape the Underworld and arrive in Santa Monica with the help of the magical pearls. They realize they have been manipulated by Ares and Percy confronts him about stealing the bolt and the helm. The two engage in battle. Percy defeats Ares after stabbing him in the heel. Rather than continue fighting, Ares accepts defeat but points out that Percy has made a new enemy. The Furies appear and return the Helm of Darkness to Hades while Percy, Annabeth, and Grover head to Olympus to return the bolt to Zeus.
# Percy returns the bolt to Zeus on Mount Olympus and meets his father, Poseidon. Percy informs them of his quest and shares his concerns about the mysterious pit, but Zeus dismisses the conversation. He rewards Percy by sparing his life. Before returning home, Percy has a brief conversation with Poseidon about his mother who is safely back home. Percy learns that he has a decision to make regarding a package Poseidon has sent back to him. At home, Percy shares the details of his quest with his mother and discovers that the package with Medusa’s head has been returned to him. Before leaving for camp, he encourages his mother to use it on Smelly Gabe. Percy returns to Camp Half-Blood for the rest of the summer. While there, he learns his mother used Medusa to turn Smelly Gabe into a statue as she no longer needs to put up with him to keep Percy safe. She sells the statue and uses some of the money to enroll Percy in a new private school for the fall. Before the end of the summer, Percy learns that Luke was really the one responsible for stealing the master bolt and the Helm of Darkness in order to serve Kronos, a Titan and the father of Zeus. After Chiron tells Percy justice will be restored when the time is right, Percy makes plans to confront Luke the following summer.
#"""
fhand=open("Transcripts/transcript.txt", 'r')
tra=fhand.read()
text =tra

checkpoint = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)


nltk.download('punkt')
sentences = nltk.tokenize.sent_tokenize(text)

length = 0
chunk = ""
chunks = []
count = -1
for sentence in sentences:
    count += 1
    combined_length = len(tokenizer.tokenize(sentence)) + length

    if combined_length <= tokenizer.max_len_single_sentence:
        chunk += sentence + " "
        length = combined_length

        if count == len(sentences) - 1:
            chunks.append(chunk.strip())

    else:
        chunks.append(chunk.strip())
        length = 0
        chunk = ""
        chunk += sentence + " "
        length = len(tokenizer.tokenize(sentence))
len(chunks)

inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

for input in inputs:
    output = model.generate(**input)
    print(tokenizer.decode(*output, skip_special_tokens=True))
