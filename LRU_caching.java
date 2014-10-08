/* 2012 Problem F: LRU Caching.
 *
 * Simulate LRU caching.
 */

import java.io.*;
import java.util.*;

public class LRU_caching {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("lru.in"));
        Scanner intReader = new Scanner(new File("lru.in"));
        String line;

        int capacity; // Size of cache -- from 1-26.
        int lineLength;
        char currChar;
        Object[] printableCache;
        int lineIndex = 1;
        int cacheIndex;
        
        line = scanner.nextLine();
        LinkedList<Character> cache = new LinkedList<Character>();
        
        // '0' marks end of input.
        while(!line.equals("0")) {
            capacity = intReader.nextInt();
            intReader.nextLine();
            //System.out.printf("N is %d\n", capacity);
            lineLength = line.length();
            
            System.out.printf("Simulation %d\n", lineIndex);
            
            for (int i = 2; i < lineLength; ++i) {
                currChar = line.charAt(i);
                if (currChar != '!') {
                    // Cache has room.
                    if (cache.size() < capacity) {
                        // Check if already contains.
                        if (cache.contains(currChar)) {
                            cacheIndex = cache.indexOf(currChar);
                            // If so, remove and put back on.
                            cache.remove(cacheIndex);
                            //cache.remove(currChar);
                            cache.add(currChar);
                        }
                        // Else just add to end.
                        else {
                            cache.add(currChar);
                        }
                    }
                    // No room, remove least-recently-used.
                    else {
                        if (cache.contains(currChar)) {
                            cacheIndex = cache.indexOf(currChar);
                            // If so, remove and put back on.
                            cache.remove(cacheIndex);
                            //cache.remove(currChar);
                            cache.add(currChar);
                        }
                        else {
                            cache.remove();
                            cache.add(currChar);
                        }
                    }
                }
                // currChar is '!'.
                else {
                    printableCache = cache.toArray();
                    for (int j = 0; j < cache.size(); ++j) {
                        if (printableCache[j].equals(' ')) {
                            continue;
                        }
                        System.out.print(printableCache[j]);
                    }
                    System.out.println();
                }   
                //System.out.print(currChar);
            }
            
            line = scanner.nextLine();
            ++lineIndex;
            cache.clear();
        }
    }
}
            
            
