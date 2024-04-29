module PBL(umid_ar, umid_solo, temp, gotejamento,aspersao, h,m,l,erro,alarme,valvula,S, Saida_A_Digito, Saida_B_Digito, Saida_C_Digito, Saida_D_Digito, Saida_E_Digito, Saida_F_Digito, Saida_G_Digito);
    
	input umid_ar, umid_solo, temp, h, m, l, S;
	output gotejamento, aspersao, erro, alarme, valvula,Saida_A_Digito, Saida_B_Digito, Saida_C_Digito, Saida_D_Digito, Saida_E_Digito, Saida_F_Digito, Saida_G_Digito;
   
	wire Caixa_A, Caixa_B, Caixa_C, Caixa_D, Caixa_E, Caixa_F, Caixa_G;
	wire Aciona_A, Aciona_B, Aciona_C, Aciona_D, Aciona_E, Aciona_F, Aciona_G;
	
	wire F1, F2, F3, F4,F5,er;
	wire A1, A2,A3,A4,A5,A6;
	wire E1, E2, E3, E4;
	wire As1, As2,X1,X2;
    
	not(F1,umid_solo);
	not(F5,umid_ar);
	not(F2, m);
	not(A2,m);
	not(A6,h);
	not(A3,l);
	not(A4,temp);
    
	//Sistema de Gotejamento
	or(F3,F2,temp);
	and(gotejamento,F1,umid_ar,F3,X2);
    
	// Sistema de Aspersao
	and(As1,m,A4,F1);
	and(As2,F1,F5);
	or(X1, As2, As1);
     not(X2,alarme);
     and(aspersao, X1,X2);
    
	not(E1,m);
	not(E2,l);
    
	and(E3,h,E1);
	and(E4,m,E2);
    
	// Erro
	or(erro,E3,E4);
	not(er,erro);
    
	//Alarme
	or(alarme,E2,erro);
    
	//Valvula de Agua
	and(valvula,er,A6);
	// ----------------------------------------------------
	// Chamando o Codificador da Caixa D'água
	CodificaCxa Caixa(
	.h(h),
	.m(m),
	.l(l),
	.Caixa_A(Caixa_A),
	.Caixa_B(Caixa_B),
	.Caixa_C(Caixa_C),
	.Caixa_D(Caixa_D),
	.Caixa_E(Caixa_E),
	.Caixa_F(Caixa_F),
	.Caixa_G(Caixa_G)
	);
	
	// Chamando o Codificador dos Acionamentos de Irrigação
	CodificaAciona Aciona(
	.gotejamento(gotejamento),
	.aspersao(aspersao),
	.Aciona_A(Aciona_A),
	.Aciona_B(Aciona_B),
	.Aciona_C(Aciona_C),
	.Aciona_D(Aciona_D),
	.Aciona_E(Aciona_E),
	.Aciona_F(Aciona_F),
	.Aciona_G(Aciona_G)
	);

	// Multiplexadores >>>
	
	Multiplexador Mux1(
	.acio(Aciona_A),
	.cxa(Caixa_A),
	.S(S),
	.X(Saida_A_Digito)
	);
	
	Multiplexador Mux2(
	.acio(Aciona_B),
	.cxa(Caixa_B),
	.S(S),
	.X(Saida_B_Digito)
	);
	
	Multiplexador Mux3(
	.acio(Aciona_C),
	.cxa(Caixa_C),
	.S(S),
	.X(Saida_C_Digito)
	);
	
	Multiplexador Mux4(
	.acio(Aciona_D),
	.cxa(Caixa_D),
	.S(S),
	.X(Saida_D_Digito)
	);
	
	Multiplexador Mux5(
	.acio(Aciona_E),
	.cxa(Caixa_E),
	.S(S),
	.X(Saida_E_Digito)
	);
	
	Multiplexador Mux6(
	.acio(Aciona_F),
	.cxa(Caixa_F),
	.S(S),
	.X(Saida_F_Digito)
	);
	
	Multiplexador Mux7(
	.acio(Aciona_G),
	.cxa(Caixa_G),
	.S(S),
	.X(Saida_G_Digito)
	);
	
endmodule


