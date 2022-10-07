def basedir():
    root = os.path.abspath(os.sep)
    base_dir = root + "Users\\Guilherme\\Documents"
    return base_dir

def get_projects_list():
    os.chdir(basedir() + "\\testes")
    file_list = []
    for f in os.listdir():
        file_list.append(f)
    return file_list
    
def generate_sheet():
    data = {"file_names": get_projects_list()}
    file_df = pd.DataFrame(data)
    new_directory = basedir() + "\\testes\\automation_tests\\sheets\\projetos"
    today = date.today()
    file_df.to_excel(new_directory + "-lista-arquivos" + str(today) + ".xlsx")
    return file_df

def main():
    sheet = generate_sheet()
    print("Criando planilha de arquivos de projetos...")
    sleep(1.5)
    print("Planilha criada.")
    q = input("Deseja acessar tabela de arquivos? (s/n): ")
    if "s".lower() in q:
        print(sheet["file_names"])
        input(" ")


if __name__=="__main__":
    import os
    import pandas as pd
    from time import sleep
    from datetime import date

    main()