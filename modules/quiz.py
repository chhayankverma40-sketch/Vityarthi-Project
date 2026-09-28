import json
from pathlib import Path
FILE=Path(__file__).resolve().parent.parent/"data"/"questions.json"

def run_quiz():
    q=json.loads(FILE.read_text())
    score=0
    print("\n=== BIO QUIZ LAB ===")
    for i,item in enumerate(q,1):
        print(f"\n{i}. {item['question']}")
        for k,v in item["options"].items(): print(f"  {k}. {v}")
        if input("Answer: ").upper().strip()==item["answer"]:
            print("Correct!"); score+=1
        else: print("Incorrect. Answer:",item["answer"])
    print(f"Score: {score}/{len(q)} | Accuracy: {score/len(q)*100:.1f}%")
