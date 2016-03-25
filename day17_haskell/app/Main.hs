module Main where

parse_file :: String -> [Int]
parse_file xs = map read $ words xs


count_combinations :: Int -> [Int] -> Int
count_combinations _ []
  = 0
count_combinations ltr (c:cs)
  = result1 + result2
  where
  remaining_ltr
    = ltr - c
  result1
    = if remaining_ltr > 0
        then count_combinations remaining_ltr cs
      else if remaining_ltr == 0
        then 1
      else 0
  result2
    = count_combinations ltr cs

main :: IO ()
main
  = do
    file_content <- readFile "input.txt"
    let containers = parse_file file_content
    putStrLn $ "input: " ++ (show containers)
    let number_solutions = count_combinations 150 containers
    putStrLn $ "number of solutions: " ++ (show number_solutions)
