import cartopy
import cartopy.crs as ccrs

# to standardize plots
PROJECTION = ccrs.Mercator()


def make_plot(da, ax=None, plot_kwargs={}):

    if ax is None:
        ax = plt.gca()
    
    # make the actual plot
    da.plot.pcolormesh(ax=ax, transform=ccrs.PlateCarree(), **plot_kwargs)
    
    # geometries
    ax.coastlines();
    ax.add_feature(cartopy.feature.OCEAN, facecolor='lightgrey')
    ax.add_feature(cartopy.feature.BORDERS)
    
    # grid lines
#     gl = ax.gridlines(draw_labels=True, linewidth=0)
#     gl.xlabels_top = False
#     gl.ylabels_left = False
    
    # boundaries
    states_provinces = cartopy.feature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    ax.add_feature(states_provinces, edgecolor='gray')
    return ax


def add_ylabel(ax, text, fontsize=12):
    return ax.text(-0.07, 0.55, text, va='center', ha='center',
        rotation='vertical', rotation_mode='anchor',
        transform=ax.transAxes, fontsize=fontsize)