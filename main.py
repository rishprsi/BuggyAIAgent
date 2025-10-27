import sys

from client import call_llm

def main(prompt="",debug_mode=False):
    print("Hello from buggyaiagent!")
    call_llm(prompt,debug_mode)


if __name__ == "__main__":
    # print(sys.argv)
    debug_mode = False
    prompt = ""
    for i in range(1,len(sys.argv)):
        if sys.argv[i]=="--verbose":
            debug_mode = True
        elif type(sys.argv[i]) == str:
            prompt = sys.argv[i]
    if len(sys.argv) >1:
        main(prompt,debug_mode)
    else:
        raise Exception("No prompt provided",debug_mode)
