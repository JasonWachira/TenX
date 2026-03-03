import { useRouter } from "@tanstack/react-router"
import { HouseSimpleIcon, AddressBookIcon, PersonIcon } from "@phosphor-icons/react";


const menu = [
    { name: "Home", path: "/", icon: <HouseSimpleIcon size={15}  className="inline-block" /> },
    { name: "About", path: "/about", icon: <AddressBookIcon size={15}  className="inline-block" /> },
    {name:"Candidates", path: "/candidates", icon: <PersonIcon size={15}  className="inline-block" />},
]


function NavigationTop() {
    const router = useRouter()

    return (
        <nav className="w-full text-sm mb-6 px-4 py-2 flex flex-col sm:flex-row sm:justify-between items-center   gap-2 sm:gap-0">
            <h1 className="font-bold text-lg mb-2 sm:mb-0 text-center sm:text-left">Finance Watch Project</h1>
            <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-4">
                {menu.map((item) => (
                    <a
                        key={item.path}
                        className={`nav-link flex items-center transition-all hover:bg-gray-200 rounded-md px-3 py-2 duration-150 text-base ${item.path === router.state.location.pathname ? 'bg-gray-300' : ''}`}
                        href={item.path}
                    >
                        {item.icon}
                        <span className="hidden xs:inline-block">{item.name}</span>
                    </a>
                ))}
            </div>
        </nav>
    )
}



function NavigationBottom() {
    return (
        <footer className="bottom-0 text-xs w-full rounded-md text-gray-400 mt-6">
            <div className="container mx-auto text-center">
                <p>© {new Date().getFullYear()} Finance Watch Project. All rights reserved.</p>
            </div>
        </footer>
    )
}


export { NavigationTop, NavigationBottom }