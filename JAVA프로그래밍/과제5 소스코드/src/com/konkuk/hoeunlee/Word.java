package com.konkuk.hoeunlee;

public class Word implements Comparable<Word> {
    String eng;
    String kor;
    int count;

    public Word(String eng, String kor) {
        super();
        this.eng = eng;
        this.kor = kor;
        this.count = 0;
    }

    @Override
    public String toString() {
        return eng + " : " + kor;
    }

    public void CountUp() {
        this.count = this.count + 1;
    }

    @Override
    public int compareTo(Word o) {
        return (this.count - o.count) * -1;
    }
}
