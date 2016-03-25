module Main where

import qualified Data.Map as MAP

parse_file :: String -> [Int]
parse_file xs = map read $ words xs


valid_combinations :: Int -> [Int] -> [[Int]]
valid_combinations _ []
  = []
valid_combinations ltr (c:cs)
  = result1 ++ result2
  where
  remaining_ltr
    = ltr - c
  result1
    = if remaining_ltr > 0
        then map ((:)c) $ valid_combinations remaining_ltr cs
      else if remaining_ltr == 0
        then [[c]]
      else []
  result2
    = valid_combinations ltr cs

get_min_solutions :: [[Int]] -> (Int, Integer)
get_min_solutions solutions
  = head $ MAP.toAscList $ MAP.fromListWith (+) solution_lengths
  where
  solution_lengths = map (\s -> (length s, 1)) solutions
  

main :: IO ()
main
  = do
    file_content <- readFile "input.txt"
    let containers = parse_file file_content
    putStrLn $ "input: " ++ (show containers)
    let solutions = valid_combinations 150 containers
    putStrLn $ "number of solutions: " ++ (show $ length solutions)
    let min_solutions = get_min_solutions solutions
    putStrLn $ "length of min solution: " ++ (show $ fst min_solutions) ++ " - count: " ++ (show $ snd min_solutions)
