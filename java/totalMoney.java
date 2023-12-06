public class totalMoney {

    /*
1716. Calculate Money in Leetcode Bank. Easy


Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday,
he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
    */



    public static int totalMoney(int n){
        
        int total = 0; //counter of money
        int weeks = n/7; // entire weeks
        int singleDays= n%7; // single days not conforming a week


        //a summatory of the first week is 1+2+3+4+5+6+7=28
        //start the next Monday adding 1 dollar more and add from this
        // is the same that add 1 dollar each day of the week
        for (int i=0;i<weeks;i++) total += 28+7*i;

        //for single days, just the number of the day + the index of the week
        for( int i=1;i<=singleDays;i++) total += i+1*weeks;

        return total;
    }


	public static void main(String[] args) {		
            int daysToSave=1000;
            int dinerets=totalMoney(daysToSave);
	}

}
