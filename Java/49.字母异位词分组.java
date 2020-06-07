/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) {
            return new ArrayList<>();
        }
        Map<String, List> res = new HashMap<>();

        for (String str : strs) {
            char[] c = str.toCharArray();
            Arrays.sort(c);
            String cs = String.valueOf(c);
            if (!res.containsKey(cs)) 
                res.put(cs, new ArrayList<>());
    
            res.get(cs).add(str);

        }
        return new ArrayList(res.values());

    }
}
// @lc code=end

