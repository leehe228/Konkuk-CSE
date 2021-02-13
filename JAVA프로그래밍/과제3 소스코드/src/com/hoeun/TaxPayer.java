package com.hoeun;

public class TaxPayer {
	
	protected String name;
	protected String number;
	protected int earnings;
	
	public TaxPayer(String name, String number, int earnings) {
		this.name = name;
		this.number = number;
		this.earnings = earnings;
	}
	
	public double getTax() {
		return earnings * 0.1;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setNumber(String number) {
		this.number = number;
	}
	
	public void setEarnings(int earnings) {
		this.earnings = earnings;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getNumber() {
		return this.number;
	}
	
	public int getEarnings() {
		return this.earnings;
	}
	
	@Override
	public String toString() {
		return "이름: " + this.name + "\n식별번호: " + this.number + "\n소득금액: " + this.earnings + "\n";
	}
	
}
