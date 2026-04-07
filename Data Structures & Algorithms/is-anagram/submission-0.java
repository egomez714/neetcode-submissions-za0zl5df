class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false; 
        }
        
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); ++i){
            char c = s.charAt(i); 
            if(map.containsKey(c)){
                map.put(c,map.get(c) + 1);
            }
            else{
                map.put(c, 1);
            }
        }
        for (int j = 0; j < t.length(); ++j){
            char b = t.charAt(j);
            if (map.containsKey(b)){
                map.put(b,map.get(b) - 1);
            }
            else{
                return false;
            }
        }
        for (int values : map.values()){
            if (values != 0){
                return false;
            }
        }
        return true;
    }
}
