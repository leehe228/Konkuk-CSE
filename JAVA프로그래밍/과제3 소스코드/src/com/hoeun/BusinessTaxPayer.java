package com.hoeun;

public class BusinessTaxPayer extends TaxPayer{
	private int expenses;
	
	public BusinessTaxPayer(String name, String number, int earnings, int expenses) {
		super(name, number, earnings);
		this.expenses = expenses;
	}
	
	@Override
	public double getTax() {
		double taxableAmount = (double)(earnings - expenses);
		
		if (taxableAmount <= 0)
			return 0.0;
		
		else if(taxableAmount >= 4000)
			return taxableAmount * 0.2;
		
		else 
			return taxableAmount * 0.1;
	}
	
	@Override
	public String toString() {
		return super.toString() + "총 지출액: " + this.expenses + "\n";
	}
}
