class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()){
            return false;
        }
        if(s.equals(t)){
            return true;
        }

        HashMap<Character, Integer> sStr = new HashMap<>();
        HashMap<Character, Integer> tStr = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);
            System.out.println(curr);
            if (sStr.containsKey(curr)){
                sStr.put(curr, sStr.get(curr) + 1);
            }
            else{
                sStr.put(curr, 1);
            }
        }
        
        for(int i = 0; i < t.length(); i++){
            char curr = t.charAt(i);
            System.out.println(curr);
            if (tStr.containsKey(curr)){
                tStr.put(curr, tStr.get(curr) + 1);
            }
            else{
                tStr.put(curr, 1);
            }
        }

        for(int i = 0; i < s.length(); i++){
            if((sStr.get(s.charAt(i)) != tStr.get(s.charAt(i)))){
                return false;
            }
        }

        return true;
    }
}
