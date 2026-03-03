
import { UserCircleIcon } from "@phosphor-icons/react"
import { useQuery } from "@tanstack/react-query"
import { BarChart } from '@mui/x-charts/BarChart';
type Candidate = {
    id: string,
    name: string,
    experience: number,
    skills: string[]
}


function CandidateCard({ candidateId }: { candidateId: string }) {

    async function getCandidate(){
        // Replace with your actual API endpoint
        return [
            {
                id: candidateId,
                name: "John Doe",
                party: "Democratic",
                experience: 5,
                donations: 100000,
                skills: ["Public Speaking", "Policy Analysis", "Campaign Management"]
            }
        ]
    }
    const { data, isLoading, error } = useQuery({
        queryKey: ['candidate', candidateId],
        queryFn: getCandidate
    })
        
    return (
        <div className="bg-gray-200 rounded-md p-6 sm:p-8 md:p-12 w-full max-w-3xl mx-auto">
            {isLoading ? <div>Loading...</div>
            : error ? <div>Error loading candidate data</div>
            : data ? (
                <div className="flex flex-col md:flex-row md:justify-between md:items-center gap-6 md:gap-10">
                    <div className="flex flex-col items-center md:items-start md:flex-row gap-4 md:gap-8 w-full">
                        <UserCircleIcon size={80} className="text-gray-400 shrink-0" />
                        <div className="flex sm:flex-row flex-col items-center md:items-start">

                            <div>
                            <h2 className="text-xl md:text-2xl font-bold text-center md:text-left">{data[0].name}</h2>
                            <p className=" text-center md:text-left">Party: {data[0].party}</p>
                            <p className=" text-center md:text-left">Experience: {data[0].experience} years</p>
                            <p className=" text-center md:text-left">Donations: ${data[0].donations.toLocaleString()}</p>
                         
                            </div>

                        
                                
                         
                       
                        </div>
                    </div>
                </div>
            ): null}


            <div className="mt-6 text-center md:text-left">
                <BarChart
                xAxis={[
                    {
                    id: 'barCategories',
                    scaleType: 'band',
                    data: ['bar A', 'bar B', 'bar C'],
                    height: 28,
                    },
                ]}
                series={[
                    {
                    data: [2, 5, 3],
                    },
                ]}
                height={300}
                />
            </div>
        </div>
    )
}
          

export default CandidateCard