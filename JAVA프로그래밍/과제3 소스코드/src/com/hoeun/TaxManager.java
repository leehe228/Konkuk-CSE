package com.hoeun;

public class TaxManager{
	
	private String city;
	private int number;
	private TaxPayer[] payer;
	private int count;
	
	public TaxManager(String city, int number) {
		this.city = city;
		this.number = number;
		this.count = 0;
		payer = new TaxPayer[this.number];
	}
	
	public void addTaxPayer(TaxPayer taxPayer) {
		if (this.count < this.number){
			payer[this.count] = taxPayer;		
			this.count++;
		} else {
			System.err.println("더 이상 입력할 수 없습니다.");
		}
	}
	
	public void showTax() {
		double sum = 0;
		for (int i = 0; i < count; i++) {
			sum += payer[i].getTax();
		}
		
		System.out.printf("%s 지역의 총 세금 징수액은 %.2f입니다.\n", this.city, sum);
	}
	
	public void showSalaryTaxPayer() {
		System.out.println("**** 근로소득자의 징수내역 ****");
		
		double sum = 0;
		
		for(int i = 0; i < count; i++) {
			if(payer[i].getClass() == SalaryTaxPayer.class) {
				SalaryTaxPayer temp = (SalaryTaxPayer)payer[i];
				System.out.print(temp);
				System.out.println("세금액: " + temp.getTax());
				System.out.println("--------------------");
				sum += temp.getTax();
			}
		}
		
		System.out.printf("총 근로소득세 징수금액: %.2f\n", sum);
	}
	
	public void showBusinessTaxPayer() {
		System.out.println("**** 사업소득자의 징수내역 ****");
		
		double sum = 0;
		
		for(int i = 0; i < count; i++) {
			if(payer[i].getClass() == BusinessTaxPayer.class) {
				BusinessTaxPayer temp = (BusinessTaxPayer)payer[i];
				System.out.print(temp);
				System.out.println("세금액: " + temp.getTax());
				System.out.println("--------------------");
				sum += temp.getTax();
			}
		}
		
		System.out.printf("총 사업소득세 징수금액: %.2f\n", sum);
	}
}
