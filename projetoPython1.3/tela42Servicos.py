from tkinter import *
from tkinter import ttk
from bancoDeDadosP import *
from tkinter import messagebox

banco = Banco()


class Tela42:
    def __init__(self):

        self.janela42 = Tk()

        "Configurando_Janela=============================================================="

        self.janela42.title("Amilton Carvalho")
        self.janela42.geometry("1366x768")
        self.janela42.config(bg="black")
        self.janela42.state("zoomed")

        "Tipando_Variáveis=============================================================="

        # Tipando as variaveis

        self.digNome = StringVar()
        self.digPlaca = StringVar()
        self.digTelefone = StringVar()
        self.digEmail = StringVar()
        self.digServico = StringVar()

        "Janela_Tkinter=============================================================="

        self.frame1 = Frame(self.janela42, bg="black")
        self.frame1.grid(row=0, column=0, padx=5, sticky="n")

        self.frame2 = Frame(self.janela42, bg="black")
        self.frame2.grid(row=0, column=1)

        "Frame_Título=============================================================="

        self.titulo = Label(self.frame1, text="Cadastramento de Serviços",
                            bg="black", fg="white", font=("Calibri", 18, "bold"), width=25)
        self.titulo.grid(row=0, padx=20, pady=10)

        "Frame_Logo=============================================================="

        #self.imgLogo = PhotoImage(file="Imagens\\amiltonCarvalhoLogo.png")

        #self.logo = Label(self.frame1, image=self.imgLogo, bg="black")
        #self.logo.grid(row=1, column=0)

        "Frame_Dados=============================================================="

        self.frameDados = Frame(self.frame1, bg="black")
        self.frameDados.grid(row=2, column=0)

        self.labNome = Label(self.frameDados, text="Nome:",
                             bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labNome.grid(row=0, column=0, padx=10, pady=10)

        self.entNome = Entry(
            self.frameDados, textvariable=self.digNome, font=("Calibri", 13))
        self.entNome.grid(row=0, column=1, padx=10, pady=10)

        self.labPlaca = Label(self.frameDados, text="Placa:",
                              bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labPlaca.grid(row=1, column=0, padx=10, pady=10)

        self.entPlaca = Entry(
            self.frameDados, textvariable=self.digPlaca, font=("Calibri", 13))
        self.entPlaca.grid(row=1, column=1, padx=10, pady=10)

        self.labTelefone = Label(self.frameDados, text="Telefone:",
                                 bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labTelefone.grid(row=2, column=0, padx=10, pady=10)

        self.entTelefone = Entry(
            self.frameDados, textvariable=self.digTelefone, font=("Calibri", 13))
        self.entTelefone.grid(row=2, column=1, padx=10, pady=10)

        self.labEmail = Label(self.frameDados, text="E-mail:",
                              bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labEmail.grid(row=3, column=0, padx=10, pady=10)

        self.entEmail = Entry(
            self.frameDados, textvariable=self.digEmail, font=("Calibri", 13))
        self.entEmail.grid(row=3, column=1, padx=10, pady=10)

        self.labServico = Label(self.frameDados, text="Servico:",
                                bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labServico.grid(row=4, column=0, padx=10, pady=10)

        self.entServico = Entry(
            self.frameDados, textvariable=self.digServico, font=("Calibri", 13))
        self.entServico.grid(row=4, column=1, padx=10, pady=10)

        "Frame_Botões=============================================================="

        self.frameBotoes = Frame(self.frame2, bg="black")
        self.frameBotoes.grid(row=0, column=0, pady=30)

        self.botaoProcurar = Button(self.frameBotoes, text="Buscar", command=self.buscarServicos, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=10)
        self.botaoProcurar.grid(row=0, column=0, padx=10, pady=10)

        self.botaoVer = Button(self.frameBotoes, text="Exibir Todos", command=self.exibirTodos, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=12)
        self.botaoVer.grid(row=0, column=1, padx=10, pady=10)

        self.botaoInserir = Button(self.frameBotoes, text="Cadastrar Serviço", command=self.adicionarServicos,
                                   bg="red", fg="white", font=("Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=20)
        #self.botaoInserir.grid(row=0, column=2, padx=10, pady=10)

        self.botaoAtualizar = Button(self.frameBotoes, text="Alterar Serviço", command=self.editarServicos,
                                     bg="red", fg="white", font=("Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=17)
        self.botaoAtualizar.grid(row=0, column=3, padx=10, pady=10)

        self.botaoDeletar = Button(self.frameBotoes, text="Excluir Serviço", command=self.deletarServicos,
                                   bg="red", fg="white", font=("Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=20)
        self.botaoDeletar.grid(row=0, column=4, padx=10, pady=10)

        "Frame_Botão_Limpar=============================================================="

        self.frameLimpar = Frame(self.frame1, bg="black")
        self.frameLimpar.grid(row=3, column=0)

        self.botaoLimpar = Button(self.frameLimpar, text="Limpar Campos", command=self.limparCampos, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botaoLimpar.grid(row=1, column=2, padx=10, pady=40)

        "Frame_Treeview=============================================================="

        self.frameTabela = Frame(self.frame2)
        self.frameTabela.grid(row=1, column=0)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=(
            "Calibri", 13), rowheight=50)
        self.style.configure("mystyle.Treeview.Heading",
                             font=("Calibri", 13, "bold"))

        self.tv = ttk.Treeview(self.frameTabela, columns=(
            1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")

        self.tv.heading("1", text="ID")
        self.tv.heading("2", text="Nome")
        self.tv.heading("3", text="Placa")
        self.tv.heading("4", text="Telefone")
        self.tv.heading("5", text="E-mail")
        self.tv.heading("6", text="Serviço")
        self.tv.heading("7", text="Status")
        self.tv.heading("8", text="")

        self.tv.column("1", width=40)
        self.tv.column("2", width=200)
        self.tv.column("3", width=100)
        self.tv.column("4", width=150)
        self.tv.column("5", width=200)
        self.tv.column("6", width=100)
        self.tv.column("7", width=180)
        self.tv.column("8", width=0)

        self.tv["show"] = "headings"
        self.tv.bind("<ButtonRelease-1>", self.pegarDados)

        self.tv.grid(row=0, column=0)

        self.scroolTv = Scrollbar(self.frameTabela, orient="vertical")
        self.tv.configure(yscroll=self.scroolTv.set)
        self.scroolTv.grid(row=0, column=1)

        self.exibirTodos()

        mainloop()

    def limparCampos(self):
        self.entNome.delete(0, END)
        self.entPlaca.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entServico.delete(0, END)

    def adicionarServicos(self):
        if (self.entNome.get() == "" or self.entPlaca.get() == "" or self.entTelefone.get() == "" or self.entEmail.get() == "" or self.entServico.get() == ""):
            messagebox.showwarning(
                "Erro na entrada", "Por favor, preencha todos os campos")
        else:
            banco.insertServicos(self.entNome.get(), self.entPlaca.get(
            ), self.entTelefone.get(), self.entEmail.get(), self.entServico.get())
            self.exibirTodos()
            self.limparCampos()

    def exibirTodos(self):
        self.tv.delete(*self.tv.get_children())
        for i in banco.viewServicos():
            self.tv.insert("", END, values=i)

    def pegarDados(self, event):
        # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
        #self.linhaSelecionada = self.tv.focus()
        self.linhaSelecionada = self.tv.selection()
        self.limparCampos()
        # pega o item(funcionário) que está nessa linha da tabela e atribue a uma variavel(self.dados)
        self.dados = self.tv.item(self.linhaSelecionada)
        global linha  # torna a variavel global para usala futuramente
        linha = self.dados["values"]  # valores da linha selecionada
        self.digNome.set(linha[1])
        self.digPlaca.set(linha[2])
        self.digTelefone.set(linha[3])
        self.digEmail.set(linha[4])
        self.digServico.set(linha[5])

    def editarServicos(self):
        if (self.entNome.get() == "" or self.entPlaca.get() == "" or self.entTelefone.get() == "" or self.entEmail.get() == "" or self.entServico.get() == ""):
            messagebox.showwarning(
                "Erro na entrada", "Por favor, preencha todos os campos")
        else:
            banco.updateServicos(linha[0], self.entNome.get(), self.entPlaca.get(
            ), self.entTelefone.get(), self.entEmail.get(), self.entServico.get())
            self.limparCampos()
            self.exibirTodos()

    def deletarServicos(self):
        banco.deleteServicos(linha[0])
        self.limparCampos()
        self.exibirTodos()
        pass

    def buscarServicos(self):
        self.tv.delete(*self.tv.get_children())
        linhas = banco.searchServicos(self.entNome.get(), self.entPlaca.get(
        ), self.entTelefone.get(), self.entEmail.get(), self.entServico.get())
        for i in linhas:
            self.tv.insert("", END, values=i)


#Tela42()
