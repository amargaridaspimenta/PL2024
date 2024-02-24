import re
import sys

def main():
    input_file = "texto.md"
    output_file = "output.txt"

    with open(input_file, "r") as file, open(output_file, "w") as output:
        for line in file:
            line = line.strip()  
            if not line:  
                continue
            total = 0
            
            print("Texto do arquivo:", line.strip())
            print("Texto do arquivo:", line.strip(), file=output)  
            
            words = re.findall(r'\b\w+\b', line)  
            active = True
            
            for word in words:
                if "on" in word.lower():
                    active = True
                elif "off" in word.lower():
                    active = False
                elif word == "=":
                    if active:
                        print("Soma total:", total)
                        print("Soma total:", total, file=output)  
                    else:
                        print("Erro: 'ON' está desativado.")
                        print("Erro: 'ON' está desativado.", file=output)  
                elif active and word.isdigit():
                    total += int(word)
            
            print("Soma total:", total)
            print("Soma total:", total, file=output)  

if __name__ == "__main__":
    main()
