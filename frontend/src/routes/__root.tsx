import { Outlet, createRootRoute } from '@tanstack/react-router'
import { TanStackRouterDevtoolsPanel } from '@tanstack/react-router-devtools'
import { TanStackDevtools } from '@tanstack/react-devtools'
import {NavigationTop, NavigationBottom} from '../components/navigation'
import '../styles.css'


export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
    <>
    <NavigationTop />
      <Outlet />
      <TanStackDevtools
        config={{
          position: 'bottom-right',
        }}
        plugins={[
          {
            name: 'TanStack Router',
            render: <TanStackRouterDevtoolsPanel />,
          },
        ]}
      />
      <NavigationBottom />
    </>
  )
}
