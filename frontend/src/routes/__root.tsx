import { Outlet, createRootRoute } from '@tanstack/react-router'
import { TanStackRouterDevtoolsPanel } from '@tanstack/react-router-devtools'
import { TanStackDevtools } from '@tanstack/react-devtools'

import '../styles.css'
import { NavigationTop, NavigationBottom } from '#/components/navigation'

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
