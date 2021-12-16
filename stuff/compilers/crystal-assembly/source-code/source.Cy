class main():

    function @default():
        INT num = $input("enter an integer")
        loop i, while i < num, i += 1:
            $output(@secondary(i))
            $output(STR "hello world")
            INT out = @sus($input("enter another integer"))
        &return()

    function @secondary(i):
        INT x = i + i
        INT y = i - x
        &return(y)

    function @sus(sheesh):
        loop i, while i < 100, i += 1
            if sheesh < i:
                $output(sheesh, "is smaller than", i)
            else-if sheesh == i:
                $output(sheesh, "is equal to", i)
                &break-loop()
            INT variable1 = $multiply(sheesh, sheesh)
        &return(variable1)
