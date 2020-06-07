import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=557 lang=java
 *
 * [557] 反转字符串中的单词 III
 */

// @lc code=start
public class Solution {
    public String reverseWords(String s) {
        String words[] = s.split(" ");
        StringBuilder res=new StringBuilder();
        for (String word: words)
            res.append(new StringBuffer(word).reverse().toString() + " ");
        return res.toString().trim();
    }
}

// class Solution {
//     public String reverseWords(String s) {
//         String[] sa = s.split("\\s+");
//         for (int i=0; i<sa.length; i++) {
//             sa[i] =  convert(sa[i]);
//         }
//         return String.join(" ", sa);
//     }

//     private String convert(String s) {
//         char[] cs = s.toCharArray();
//         int i=0;
//         int j= cs.length -1;
//         char c;
//         while (true) {
//             if (i >= j) {
//                 break;
//             }   
//             c = cs[i];
//             cs[i] = cs[j];
//             cs[j] = c;
//             i++;
//             j--;
//         }
//         return new String(cs);
//     }
// }

// class Solution {
//     public String reverseWords(String s) {
//         char[] charArr = s.toCharArray();
        
//         for(int i=0;i<charArr.length;i++) {
//             int j = i;
//             while((j != charArr.length - 1) && (charArr[j] != ' ')) {
//                 j++;
//             }
            
//             int k = i;
//             int l = j;
            
//             if(charArr[j] == ' ') {
//                j = j - 1;
//             }
            
//             while(k < j) {
//                 if(charArr[k] != charArr[j]) {
//                     char temp = charArr[k];
//                     charArr[k] = charArr[j];
//                     charArr[j] = temp;                       
//                 }
//                 k++;
//                 j--;                
//             }
            
//             i = l;       
            
//         }
        
//         return new String(charArr);        
//     }
// }

//@lc code=end

