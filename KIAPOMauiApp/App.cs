using Microsoft.Maui;
using Microsoft.Maui.Controls;

namespace KIAPOMauiApp;

public class App : Application
{
    protected override Window CreateWindow(IActivationState activationState)
    {
        return new Window(new ContentPage { Content = new Label { Text = "KIAPO RRHH", HorizontalOptions = LayoutOptions.Center, VerticalOptions = LayoutOptions.Center } });
    }
}
