package com.hoeun;

public class SalaryTaxPayer extends TaxPayer {
	private String companyName;
	
	public SalaryTaxPayer(String name, String number, int earnings, String companyName) {
		super(name, number, earnings);
		this.companyName = companyName;
	}
	
	@Override
	public double getTax() {
		if (this.earnings >= 8000)
			return this.earnings * 0.2;
		
		else if(this.earnings >= 6000)
			return this.earnings * 0.15;
		
		else if(this.earnings >= 4000)
			return this.earnings * 0.1;
		
		else if(this.earnings >= 2000)
			return this.earnings * 0.05;
		
		else 
			return this.earnings * 0.01;
	}
	
	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}
	
	public String getCompanyName() {
		return this.companyName;
	}
	
	@Override
	public String toString() {
		return super.toString() + "회사이름: " + this.companyName + "\n";
	}
}
