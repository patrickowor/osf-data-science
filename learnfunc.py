def do_some_complex_maths(value, pow=5, div=10):
    ans = ((value * 7 ) ** pow ) / div
    print(f"{ans=} {value=} {pow=} {div=}\n\n")
    return ans
    

#do_some_complex_maths(10)
#do_some_complex_maths(10, 5)
#do_some_complex_maths(10, div=2)
#do_some_complex_maths(div=7, pow=2, value=3)

complex_calc = do_some_complex_maths(0.1)
val = input("say something")

if complex_calc > 10:
    print("wow that was complex", complex_calc)
else:
    print("not so complex after all", complex_calc)
print(ans)
