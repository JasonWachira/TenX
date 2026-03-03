import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/about')({
  component: About,
})

function About() {
  return (
    <main className='p-12'>
         Secret political finance risks corruption if political financing does not take place in a fair manner resulting in the lack of a level playing field among political parties, unfair representation and overall distrust in political parties and political processes more generally.[2] Lack of transparency and accountability in political financing results in opacity on who is influencing decision makers or candidates for political office. According to International IDEA, “inadequately controlled political finance is one of the most widely exploited entry points for narrow private interests to exert undue influence over politics and political decisions.”[3]
In 2017, the Organization for Economic Co-operation and Development (OECD) adopted a new legal instrument called the Recommendation on Public Integrity, which calls on countries to deal with political finance, managing conflicts of interest, lobbying transparency, asset disclosure of public officials and other aspects of anti-corruption issues in a holistic manner throughout the political cycle.[4] Similarly, the Open Government Partnership (OGP), which Kenya is a member[5], advocates adopting commitments to advance political finance transparency as part of broader national open government action plans.
     
    </main>
  )
}
