import View_IV
import Model
import tkinter as tk
from tkinter import ttk

class Controller():
    def __init__(self, root, entrys):
        self.root = root
        self.create = View_IV.Create(self.root)
        self.info = View_IV.Infos()
        self.banco = Model.Main_db(self.root)
        self.entrys = entrys

    def Puxa_dados(self):
        dados = []
        for n in self.entrys:
            dados.append(n.get().lower().strip())
        return dados

    def Data(self):
        from datetime import datetime
        data = datetime.now().strftime('%d/%m')
        return data

    def Limpar_entrys(self):
        import tkinter as tk
        # Limpa as Entrys da Tela Cadastro.
        for entry in self.entrys:
            entry.delete(0, tk.END)
        self.Limpa_label5()

    def Limpa_label5(self):
        frame = '.!frame2'
        variavel_local = self.root.nametowidget(frame)
        for n in range(5,25):
            try: 
                if f'!label{n}' in variavel_local.children:
                    frame = f'.!frame2.!label{n}'
                    variavel_local = self.root.nametowidget(frame)
                    variavel_local.destroy()
                    break
                else:
                    pass
            except Exception as error:
                print(f'Erro: {error}')
                pass

    def Func_Criar_Treeview(self, verificar=True):
        # Funçao responsavel pela criação da lista e scroll.
        frame = '.!frame3'
        self.frame_lista = self.root.nametowidget(frame)
        if verificar == True:
            self.Lista_Treeview = ttk.Treeview(
                self.frame_lista, height=3, column=(
                    "Cod PROD", "PRODUTO", "Qt PROD", "VALOR", "Cod CLIENTE", "NOME", "DATA"
                )
            )
        else:
            self.Lista_Treeview = ttk.Treeview(
                self.frame_lista, height=3, column=("Cod CLIENTE", "NOME", "TELEFONE", "EENDEREÇO", "CIDADE")
            )
        self.scroolLista = tk.Scrollbar(self.frame_lista, orient="vertical")
        self.scroolLista.place(relx=0.97, rely=0.01, relwidth=0.016, relheight=0.96)
        self.Lista_Treeview.configure(yscroll=self.scroolLista.set)
        self.Lista_Treeview.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.96)
        self.Lista_Treeview.bind("<Double-1>", self.Func_Double_Click)

    def Func_Double_Click(self, event=None):
        selection = self.Lista_Treeview.selection()
        item = self.Lista_Treeview.item(selection[0], "values")
        if len(item) == 7:
            lista = []
            for info in item:
                lista.append(info)
            lista.pop(2); lista.pop(); lista.pop()
            if 'R$ ' in lista[2]:
                alt = lista[2].replace('R$ ', ' ').strip()
                lista[2] = alt
            for entry, value in zip(self.entrys, lista):
                entry.insert(tk.END, value)
        else:
            print('nao funfo')
            pass

    def Atualiza_TreeView(self, verificar=True):
        # Atualiza a lista
        frame = '.!frame3.!treeview'
        self.Lista_Treeview = self.root.nametowidget(frame)
        self.Lista_Treeview.delete(*self.Lista_Treeview.get_children())
        for row in self.banco.Func_Select_Lista():
            if verificar:
                self.Lista_Treeview.insert(
                    "", tk.END, values=(row[0],f"{row[1]:0>3}",row[2],
                            (f"R$ {row[3]:.2f}"),row[4], row[5],row[6])
                )
            else:
                self.Lista_Treeview.insert(
                "", tk.END, values=(row[0], row[1], row[2], row[3], row[4])
                )

    def Processamento_dados_venda_1(self):
        dados_1 = self.Puxa_dados()
        variavel_cod_venda = dados_1[0]
        dados_1.pop(0)
        if ',' in dados_1[1]:
                alt = dados_1[1].replace(",", ".").strip()
                dados_1[1] = alt
        if dados_1[0] == '' or dados_1[2] == '' or int(dados_1[0]) > 6:
            return [0, 0]
        if dados_1[1] == '':
            dados_1[1] = '0'
        else:
            return [dados_1, variavel_cod_venda]

    def Processamento_dados_venda_2(self, verificar=True):
        dados_2, variavel_cod_venda = self.Processamento_dados_venda_1()
        if dados_2 == 0 and variavel_cod_venda == 0:
            return [False, 0]
        else:
            dados_2.insert(1, self.info.Info_Cod_Produto(dados_2[0]))
            variavel_local = self.banco.Puxa_nome(dados_2[3])
            if variavel_local == False:
                self.create.Func_Erro_Dados(self.root, frase='Cliente não Cadastrado')
            else:
                dados_2.append(self.banco.Puxa_nome(dados_2[3]))
                dados_2.append(self.Data())
                self.Limpa_label5()
                if verificar == True:
                    return [True, dados_2]
                else:
                    dados_2.append([variavel_cod_venda])
                    return [True, dados_2]

    def vizualizador_widget(self):
        print('----------------------------------------------')
        def listar_widgets_ativos(root):
            for widget in root.winfo_children():
                print(f"Widget: {widget}")
                print(f"Ativo: {widget.winfo_exists()}")
                print("-----------")
                if widget.winfo_children():
                    listar_widgets_ativos(widget)
        listar_widgets_ativos(self.root)

                    