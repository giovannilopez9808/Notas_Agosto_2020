      subroutine gauss(temp)
        integer, parameter:: n=2
        real*8 :: array(n), pi, temp, mean = 0, sd=1
        pi = 4.0*atan(1.0)
!<-----------Distrobucion uniforme------------------->
        call RANDOM_NUMBER(array)
!<-------------Distribucion gaussiana----------------->
        temp=sd*sqrt(-2.0*log(array(1)))* 
     & (cos(2*pi*array(2))+sin(2*pi*array(2)))+mean
      end subroutine 

      program hist
        real*8 value
        integer i
        open(1,file="data.txt")
        do i=1,100000
          call gauss(value)
          write(1,*) value
        end do
        close(1)
      end program