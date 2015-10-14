      program FATORIAL 

      end program

      subroutine fatF(N)
         implicit none
         integer i,fat,N

         fat = 1
         do i=1,N
            fat = fat *i
         enddo

         write(*,*),fat
      end
